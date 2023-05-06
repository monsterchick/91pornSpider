import os

# print(os.path.join(os.getcwd(),'download'))
def mkdir():
    # print(cur_path)
    # check if folder exists, if not, make one. if exists, prompt a message
    if not os.path.isdir("download"):
        os.makedirs("download")  # make a folder called download
        print("Folder created successfully!")
    else:
        print("Folder existed!")
        pass

# print(os.path.join(cur_path,'download'))a

def mkjson():
    # path = os.getcwd()+'\\'+'download\\data.json'
    path = os.path.join(os.getcwd(),'download')
    if not os.path.exists(path):
        with open(path,'w')as f:
            f.write('')
        print("File created successfully!")
    else:
        print("File already exists")
        pass
# print(os.getcwd()+'\\'+'data.json')    # 用于调试
