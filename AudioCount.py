import sys,os,glob


def main():
    DIR = os.path.dirname(os.path.abspath(__file__))

    target = os.path.join(DIR,"GetAudiosetSample","result")

    files=["balanced_train","eval","unblanced_train"]

    labels = os.listdir(os.path.join(target,"balanced_train"
    ))


    for fo in files:
        for label in labels:
            path = os.path.join(target,fo,label,"*")
            ans = len(glob.glob(path))
            print(fo,label,ans)





#ファイル名を投げるとファイルの内容が1行ずつ配列に入って帰ってくる
def ReadInputfile(argv):
    r=[]
    with open(argv) as f:
        for i in f.read().splitlines():
            r.append(i)
    return r

if __name__=='__main__':
    main()