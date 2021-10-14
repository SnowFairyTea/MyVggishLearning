import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import torch.optim as optim
import random
from . import myenv


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
                
    def train(self,dataloader_dict,_num_epochs=50,_print=False):
        dbprint=(lambda x:print(x)) if _print else (lambda x:None)
        #エポック数
        self.num_epochs=_num_epochs
        self.x=[]
        self.y=[]
        
        
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
                self.x.append(epoch_acc)
                self.y.append(epoch)
    

    def graph(self,_title):
        plt.plot(self.y[::2],[i.tolist() for i in self.x][::2], label="train", color ="Green")
        plt.plot(self.y[::2],[i.tolist() for i in self.x][1::2], label="valid", color ="Blue")
        plt.legend(loc='upper left')
        plt.title(_title)
        plt.show()