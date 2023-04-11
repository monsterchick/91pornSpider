import requests

def general_saving(file_path,video_url,page,working_on,title,index):
    print(f'正在保存第{page}页 第{working_on}个视频 {title}第{index + 1}个部分...')

    with open(file_path, 'ab') as f:
        res = requests.get(video_url)
        f.write(res.content)