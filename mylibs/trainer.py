import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import torch.optim as optim
import random
from . import myenv
import pandas as pd

class trainer:
    def __init__(self, 
                _classfilter=nn.Sequential(
                            nn.Linear(128,64),
                            nn.Sigmoid(),
                            nn.Linear(64,5),
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
                
    def train(self,dataloader_dict,_num_epochs=50,_print=False):
        dbprint=(lambda x:print(x)) if _print else (lambda x:None)
        #エポック数
        self.num_epochs=_num_epochs
        self.x=[]
        self.y_acc=[]
        self.y_loss=[]
        
        
        for epoch in range(self.num_epochs):
            dbprint('Epoch {}/{}'.format(epoch+1,self.num_epochs))

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

                dbprint('{} Loss: {:f} Acc: {:f}'.format(phase, epoch_loss, epoch_acc))
                self.y_acc.append(epoch_acc)
                self.x.append(epoch)
                self.y_loss.append(epoch_loss)
    

    def graph(self,_title="",acc=True,loss=True):
        if(acc):
            plt.plot(self.x[::2],[i.tolist() for i in self.y_acc][::2], label="train", color ="Green")
            plt.plot(self.x[::2],[i.tolist() for i in self.y_acc][1::2], label="valid", color ="Blue")
            plt.legend(loc='upper left')
            plt.xlabel("epoch")
            plt.ylabel("acc")
            plt.title(_title+"acc")
            plt.show()
        if(loss):
            plt.plot(self.x[::2],[i for i in self.y_loss][::2], label="train", color ="Green")
            plt.plot(self.x[::2],[i for i in self.y_loss][1::2], label="valid", color ="Blue")
            plt.legend(loc='upper left')
            plt.xlabel("epoch")
            plt.ylabel("loss")
            plt.title(_title+"loss")
    
    def eval(self, dataloader_dict,labels,mode="kondou"):
        if (mode=="0" or mode=="kondou"):
            self.kondou=np.zeros((len(labels),len(labels)))
            model=tr.model
            acc=0
            count=0.0
            for inputs,la in dataloader_dict["train"]:

                model.eval()

                output = model(inputs)
                for h in range(len(output)):
                    #print("模範解答",labels[la[h].item()])
                    ans=[[i,output[h][i].item()] for i in range(len(labels))]
                    ans.sort(key=lambda x: x[1],reverse=True)
                    acc+=1 if (ans[0][0]==la[h])else 0
                    count+=1
                    #せいかい、しゅつりょく
                    self.kondou[la[h]][ans[0][0]]+=1

        print("正解数/入力数:{}/{:.0f}".format(acc,count))
        print("正解率:{:.3f}".format(acc/count))

        
        return self.kondou
        
        elif (mode=="1"or mode=="kakuritu"):
            model=tr.model
            inputs,la = iter(dataloader_dict["train"]).__next__()
            model.eval()

            output = model(inputs)
            for h in range(len(output)):
                print("模範解答",labels[la[h].item()])
                ans=[[labels[i],output[h][i].item()] for i in range(len(labels))]
                ans.sort(key=lambda x: x[1],reverse=True)
                [print("{:7}:{:.5f}".format(ans[i][0],ans[i][1])) for i in range(len(ans))]
                print("----------------")
        
        else:
            print("mode=",mode)
            print("は未定義です")

    def getKondou(self,csvname="a"):
        df=pd.DataFrame(self.kondou)
        df.index=labels
        df.columns=labels
        df.to_csv('kondou\\'+csvname+'.csv')
        print(df)
