import os

# print(os.path.join(os.getcwd(),'save'))
def mkdir():
    # print(cur_path)
    # check if folder exists, if not, make one. if exists, prompt a message
    if not os.path.isdir("download"):
        os.makedirs("download")  # make a folder called save
        print("Folder created successfully!")
    else:
        print("Folder existed!")
        pass

# print(os.path.join(cur_path,'save'))a

def mkjson():
    # path = os.getcwd()+'\\'+'save\\data.json'
    path = os.path.join(os.getcwd(), '../save')
    if not os.path.exists(path):
        with open(path,'w')as f:
            f.write('')
        print("File created successfully!")
    else:
        print("File already exists")
        pass
# print(os.getcwd()+'\\'+'data.json')    # 用于调试
