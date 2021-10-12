import os,sys
import torch.utils.data as data
import joblib
import glob
from importlib import import_module
from . import myenv
import traceback

vggish_input=import_module(".torchvggish.vggish_input","torchvggish-master")


def get_dataloader_dict(classes,dataset_dir="GetAudiosetSample/result",batch_size=10):
    mydir=os.path.dirname(os.path.abspath(__file__))

    DataLoaderName=""

    for i in sorted(classes):
        DataLoaderName+=i
    DataLoaderName+=".jb"
    print(mydir+"\dataloaders",glob.glob(mydir+"\dataloaders\*"))
    if (mydir+"\dataloaders\\"+DataLoaderName in glob.glob(mydir+"\dataloaders\*") ):
        print("joblib.loadします")
        dataloader_dict=joblib.load(mydir+"\dataloaders\\"+DataLoaderName)
    else:
        print("新しく作ります")
        dataloader_dict=create_dataloader_dict(classes,dataset_dir,batch_size)
        # 保存
        joblib.dump(dataloader_dict, mydir+"\dataloaders\\"+DataLoaderName, compress=3)

    for x in ["train","valid"]:
        print("{}用データの数：{}".format(x,len(dataloader_dict[x])))

    return dataloader_dict

def create_dataloader_dict(classes,dataset_dir,batch_size):
    path_dict = make_path_dict(classes, dataset_dir)

    #DataSetを実際に作ってみる 
    train_dataset = MyDataset(
        path_dict=path_dict["train"],
        phase="train"
    )

    valid_dataset = MyDataset(
        path_dict=path_dict["valid"],
        phase="valid"
    )
    #print("学習用データ数 : ", len(train_dataset))
    #print("検証用データ数 : ", len(valid_dataset))
    

    train_dataloader=data.DataLoader(
        train_dataset, batch_size = batch_size, shuffle=True
    )
    valid_dataloader=data.DataLoader(
        valid_dataset, batch_size = batch_size//2, shuffle=True
    )

    dataloader_dict={
        'train': train_dataloader, 
        'valid': valid_dataloader
    }
    return dataloader_dict




def make_path_dict(classes, dataset_dir):

    #データへのファイルパスとラベルを格納したリストを取得する
    #path_dict = make_path_list()

    train_file_list=[]
    valid_file_list=[]
    for i in range(len(classes)):
        dir_name=os.path.join(dataset_dir,classes[i]).replace("\\","/")
        file_list=os.listdir(dir_name)
        
        #8割を学習用、残りを検証用にする
        num_data = len(file_list)
        num_split = int(num_data*0.8)
        
        train_file_list += [[os.path.join(dir_name, file).replace('\\', '/'), i] for file in file_list[:num_split] ]
        valid_file_list += [[os.path.join(dir_name, file).replace('\\', '/'), i] for file in file_list[num_split:]]
    return {"train":train_file_list,"valid":valid_file_list}


#print('学習データファイル数 : ', len(path_dict["train"]))
##### 先頭3件だけ表示
#print(path_dict["train"][:3])

#print('検証データファイル数 : ', len(path_dict["valid"]))
##### 先頭3件だけ表示
#print(path_dict["valid"][:3])

class MyDataset(data.Dataset):
    '''
    data_dictは[パス,番号]
    '''
    def __init__(self, path_dict,  phase='train'):
        #self.data_dict = data_dict
        self.data_dict = []
        for path, label in path_dict:
            #なんかエラー出るからむしする
            try:
                for data in vggish_input.wavfile_to_examples(path):
                    #print(1)
                    self.data_dict.append([data, label])
            except:
                print("miss!")
                
                

        
        self.phase = phase
        
    def __len__(self):
        return len(self.data_dict)
    
    def __getitem__(self,index):
        
        wav_data,label = self.data_dict[index]
        
        return wav_data, label

