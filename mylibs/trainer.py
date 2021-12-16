import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import torch.optim as optim
import random
from . import myenv
import pandas as pd
import os,sys
import numpy as np
from pathlib import Path

class trainer:
    def __init__(self, 
                _labels=["Speech","Music","Silence","Siren","Vehicle","Wind"],
                _classfilter=nn.Sequential(
                            nn.Linear(128,64),
                            nn.Sigmoid(),
                            nn.Linear(64,6),
                            nn.Softmax(dim=1)
                            ), 
                _criterion=nn.CrossEntropyLoss(),
                _optimizer = optim.SGD,#params_to_update, lr=0.01),
                _lr=0.01,
                 _weight_decay=0.0,
                _update_param_names=
                     ['classfilter.0.weight', 'classfilter.0.bias', 
                          'classfilter.2.weight','classfilter.2.bias'],
                _print=False
                ):
        '''
        _classfilter:クラスフィルタ層の中身をnn.Sequentialで宣言したものを入れる
            nn.Sequential(
                nn.Linear(128,64),
                nn.Sigmoid(),
                nn.Linear(64,5),
                nn.Softmax()
                )
        
        _num_epochs:学習時のエポック数
        
        _criterion:損失関数
        _optimizer:最適化手法
        _lr:学習の速度
        _weight_decay=重みの正規化の強さ
        _update_param_names:updateするパラメータの名前、未来が見えてないと使えないので要改造
        _print:デバッグ用出力の有無
        '''
        dbprint=(lambda x:print(x)) if _print else (lambda x:None)

        
        
        self.model = torch.hub.load('torchvggish-master_changed', 'vggish', source='local', preprocess=False,postprocess=False)
        self.model.classfilter=_classfilter

        self.labels=_labels
        
        self.model=self.model.to(myenv.device)
        self.model.eval()
        #学習させるパラメータを格納
        self.params_to_update=[]
        #対象以外は勾配計算をせず、変化しないようにもする
        for name,param in self.model.named_parameters():
            if name in _update_param_names:
                param.requires_grad = True
                self.params_to_update.append(param)
                #print("name : ",name)
            else:
                param.requires_grad = False
        
        self.lr=_lr
        self.weight_decay=_weight_decay
        self.criterion=_criterion
        self.optimizer=_optimizer(self.params_to_update, self.lr,self.weight_decay)
        dbprint(self.model)
        
        self.kondou= None
        self.x={"train":[],"valid":[]}
        self.y_acc={"train":[],"valid":[]}
        self.y_loss={"train":[],"valid":[]}
        self.num_epochs=0
                
    def train(self,dataloader_dict,_num_epochs=50,_print=False):
        dbprint=(lambda x:print(x)) if _print else (lambda x:None)
        #エポック数
        num_epochs=self.num_epochs+_num_epochs

        
        
        for epoch in range(self.num_epochs,num_epochs):
            dbprint('Epoch {}/{}'.format(epoch+1,num_epochs))

            for phase in ['train','valid']:
                if phase == 'train':
                    self.model.train()#学習モード
                else:
                    self.model.eval()#検証モード
                #epoch全体の損失の輪と正解数
                epoch_loss=0.0
                epoch_corrects=0
                count=0.0
                #dbprint(phase)
                for inputs, labels in dataloader_dict[phase]:
                    #入力の確認
                    #dbprint(len(inputs),len(labels))
                    #勾配計算を初期化する
                    self.optimizer.zero_grad()


                    with torch.set_grad_enabled(phase=='train'):
                        #labelsをcudaに
                        #dbprint(inputs.shape)
                        labels=labels.to(myenv.device)
                        inputs=inputs.to(myenv.device)
                        outputs=self.model(inputs)

                        #損失関数を計算
                        loss=self.criterion(outputs, labels)
                        #ラベルを予測
                        _,preds = torch.max(outputs,1)

                        #訓練時は逆伝搬の計算
                        if phase == "train":
                            #逆伝搬
                            loss.backward()

                            #パラメータ更新
                            self.optimizer.step()

                        #イテレーション結果の計算
                        #lossの合計を更新
                        #pytorchの使用上バッチ内の平均lossが計算されているのでデータ数をかけて合計にする
                        #損失和を「全データの損失/データ数」で求めるせいらしい?
                        #dbprint(len(inputs))
                        epoch_loss += loss.item() * inputs.size(0)

                        #正解数の合計を更新
                        epoch_corrects += torch.sum(preds == labels.data)

                #epochのlossと正解数の表示
                epoch_loss=epoch_loss/len(dataloader_dict[phase].dataset)
                epoch_acc=epoch_corrects.double()/len(dataloader_dict[phase].dataset)
                #関連数値を表示
                print("epoch_loss:{}\nepoch_corrects:{},epochsize:{}".format(epoch_loss,epoch_corrects.double(),len(dataloader_dict[phase].dataset)))

                dbprint('{} Loss: {:f} Acc: {:f}'.format(phase, epoch_loss, epoch_acc))
                self.x[phase].append(epoch)
                self.y_acc[phase].append(epoch_acc.item())
                self.y_loss[phase].append(epoch_loss)
                #配列に入れた値を確認
                #print(epoch,phase,epoch_loss)
    

    def graph(self,_title="",acc=True,loss=True):
        if(acc):
            plt.plot(self.x["train"],self.y_acc["train"], label="train", color ="Green")
            plt.plot(self.x["valid"],self.y_acc["valid"], label="valid", color ="Blue")#i.tolist()[i for i in self.y_acc["train"]]
            plt.legend(loc='upper left')
            plt.xlabel("epoch")
            plt.ylabel("acc")
            plt.title(_title+"acc")
            plt.show()
        if(loss):
            plt.plot(self.x["train"],self.y_loss["train"], label="train", color ="Green")
            plt.plot(self.x["valid"],self.y_loss["valid"], label="valid", color ="Blue")
            plt.legend(loc='upper left')
            plt.xlabel("epoch")
            plt.ylabel("loss")
            plt.title(_title+"loss")
    
    def eval(self, dataloader_dict,mode="kondou"):
        if (mode=="0" or mode=="kondou"):
            self.kondou=np.zeros((len(self.labels),len(self.labels)))
            model=self.model
            acc=0
            count=0.0
            for inputs,la in dataloader_dict["valid"]:

                model.eval()

                output = model(inputs)
                for h in range(len(output)):
                    #print("模範解答",labels[la[h].item()])
                    ans=[[i,output[h][i].item()] for i in range(len(self.labels))]
                    ans.sort(key=lambda x: x[1],reverse=True)
                    acc+=1 if (ans[0][0]==la[h])else 0
                    count+=1
                    #せいかい、しゅつりょく
                    self.kondou[la[h]][ans[0][0]]+=1

            print("正解数/入力数:{}/{:.0f}".format(acc,count))
            print("正解率:{:.3f}".format(acc/count))

            return self.kondou
        
        
        elif (mode=="1"or mode=="kakuritu"):
            model=self.model
            model.eval()

            count=0

            for inputs,la in dataloader_dict["train"]:
            

                output = model(inputs)
                for h in range(len(output)):
                    print("模範解答",self.labels[la[h].item()])
                    ans=[[self.labels[i],output[h][i].item()] for i in range(len(self.labels))]
                    ans.sort(key=lambda x: x[1],reverse=True)
                    [print("{:7}:{:.5f}".format(ans[i][0],ans[i][1])) for i in range(len(ans))]

                    plt.figure()
                    plt.imshow(inputs[h][0].to('cpu').detach().numpy().copy().T)
                    plt.title("正解："+labels[int(la[h])]+", 回答:"+labels[int(ans[h])])
                    print("----------------")
        elif (mode=="2" or mode=="spectrogram"):
            DIR=os.path.dirname(os.path.abspath(__file__))
            count=0
            os.makedirs(os.path.join(DIR,"acc"),exist_ok=True)
            os.makedirs(os.path.join(DIR,"bat"),exist_ok=True)
            model=self.model
            model.eval()

            for inputs,la in dataloader_dict["train"]:
                outputs=model(inputs)
                for i in range(len(inputs)):
                    fig=plt.figure()
                    ans=int(torch.max(outputs, 1)[1][i])
                    isans='acc' if int(la[i])== ans else 'acc'#bat
                    plt.imshow(inputs[i][0].to('cpu').detach().numpy().copy().T)
                    plt.title(""+str(int(la[i]))+":"+self.labels[ans])
                    
                    filepath=os.path.join(DIR,isans,str(count)+".png")
                    count+=1
                    fig.savefig(filepath)


        else:
            print("mode=",mode)
            print("は未定義です")

    def getKondou(self,csvname="a"):
        mydir=os.path.dirname(os.path.abspath(__file__))
        df=pd.DataFrame(self.kondou)
        df.index=self.labels
        df.columns=self.labels
        df.to_csv(os.path.join(mydir,'kondou', csvname+'.csv'))
        print(df)
    
    def saveModel(self,addname=""):
        mydir=os.path.dirname(os.path.abspath(__file__))
        classstr=str(self.model.classfilter)
        filename="".join(self.labels)+classstr.replace(".","")+addname+".pth"
        filepath=os.path.join(mydir,"models",filename.replace("\n","").replace(" ","").replace(":","").replace(",","").replace("(","").replace(")",""))
        torch.save(self.model.state_dict(), filepath)

    def loadModel(self,addname=""):
        mydir=os.path.dirname(os.path.abspath(__file__))
        classstr=str(self.model.classfilter)
        filename="".join(self.labels)+classstr.replace(".","")+addname+".pth"
        filepath=os.path.join(mydir,"models",filename.replace("\n","").replace(" ","").replace(":","").replace(",","").replace("(","").replace(")",""))
        self.model.load_state_dict(torch.load(filepath))


