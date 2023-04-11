from tqdm import tqdm
import requests

def visualize(download_list, page ,working_on, title, index, file_path, video_url):
    list = download_list
    for t in tqdm(list, desc=f'正在保存第{page}页 第{working_on}个视频 {title}第{index + 1}个部分...', unit='video'):
        with open(file_path, 'ab') as f:
            res = requests.get(video_url)
            for chunk in res.iter_content(chunk_size=4096):
                if chunk:
                    f.write(chunk)
            res.close()