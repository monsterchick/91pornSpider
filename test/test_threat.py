import requests
import threading

def download_file(url, file_name):
    # 发送GET请求获取文件内容
    response = requests.get(url)
    
    # 将文件内容写入本地文件
    with open(file_name, 'wb') as f:
        f.write(response.content)

def download_ts_files(base_url, file_names):
    # 创建线程列表
    threads = []

    for file_name in file_names:
        # 构造文件的URL
        url = f'{base_url}/{file_name}'
        
        # 创建下载线程并添加到线程列表中
        t = threading.Thread(target=download_file, args=(url, file_name))
        threads.append(t)

    # 启动所有线程
    for t in threads:
        t.start()

    # 等待所有线程完成
    for t in threads:
        t.join()

if __name__ == '__main__':
    # TS文件的基本URL
    base_url = 'http://example.com/ts-files'
    
    # TS文件名列表
    file_names = ['file1.ts', 'file2.ts', 'file3.ts']
    
    # 启动多线程下载TS文件
    download_ts_files(base_url, file_names)
