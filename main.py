import m3u8
import os
from Headers import get_headers
import requests
from bs4 import BeautifulSoup
from filter_char import avoid_spc_char


class FileHandler:
    def __init__(self):
        pass

    # print(os.path.join(os.getcwd(),'download'))
    def mkdir(self):
        # print(cur_path)
        # check if folder exists, if not, make one. if exists, prompt a message
        if not os.path.isdir("download"):
            os.makedirs("download")  # make a folder called download
            os.makedirs(os.path.join("download", "video"))  # make a folder called download
            print("Folder created successfully!")
        else:
            print("Folder already exists.")
            pass

    def mkjson(self):  # 还没通过测试
        path = os.path.join(os.getcwd(), 'download', 'data.json')
        # print('path: ',path)
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write('')
            print("File created successfully!")
        else:
            print("JSON file already exists.")


class SaveData:
    def __init__(self):
        pass

    def save_to_mp4(self, file_path, ts_download_link):
        with open(file_path, 'ab') as f:
            res = requests.get(ts_download_link)
            f.write(res.content)


class PageHandler:
    def __init__(self):
        self.headers = get_headers()
        self.savedata = SaveData()
        self.num_main_page = 0
        self.video_id = 0

    def make_url(self, num):
        url = 'https://www.91porn.com/v.php?next=watch&page={}'.format(num)
        return url

    def get_requests(self, url):
        headers = self.headers
        response = requests.get(url=url, headers=headers)
        text = response.text
        return text

    def get_ts_list(self, m3u8_url):
        m3u8_obj = m3u8.load(m3u8_url)
        ts_links = []
        for segment in m3u8_obj.segments:
            ts_links.append(segment.uri)

        return ts_links

    def get_m3u8(self, suburl):
        # res = requests.get(suburl, headers=headers)
        # txt = res.text
        text = self.get_requests(suburl)
        soup = BeautifulSoup(text, 'html.parser')
        id = soup.find('div', {'id': 'VID'}).text
        m3u8_url = f'https://cdn77.91p49.com/m3u8/{id}/{id}.m3u8'
        ts_list = self.get_ts_list(m3u8_url)
        # print('test sublink',suburl)
        return ts_list, m3u8_url  # , suburl

    def get_final_data(self, num_main_page, index_of_video, title, get_m3u8):
        ts_list = get_m3u8[0]
        # print('ts列表',ts_list)    # 用于调试
        for index, ts in enumerate(ts_list):
            # 每个ts文件的下载连接
            ts_download_link = get_m3u8[1].rsplit("/", 1)[0] + '/' + ts  # ts link for saving
            # print('ts_download_link',ts_download_link)
            print(f'正在保存第{num_main_page}页 第{index_of_video}个视频 {title}第{index + 1}个部分...')  # 最终提取的资料

            # 去除特殊字符的title
            title = avoid_spc_char(title)
            file_path = os.path.join(os.getcwd(), 'download', 'video', f'p{num_main_page}v{index_of_video}_{title}.mp4')
            # print('file path: ',file_path)

            # 保存方式：
            # 下载视频片段并保存到本地 + 可视化下载进度
            # visualize(ts,page,working_on,title,index + 1,file_path,video_url)
            # print(index)
            # 普通保存
            self.savedata.save_to_mp4(file_path=file_path, ts_download_link=ts_download_link)
            # general_saving(file_path, video_url, self.page, self.working_on, title, index)

        # 保存到json
        # save_to_json(page=page, position=working_on, title=title,preview=get_m3u8[2])

        print(f'{title}.mp4 保存成功！\n')

    def get_last_page(self):
        last_page = ''
        url = self.make_url(self.num_main_page)
        res = requests.get(url=url, headers=self.headers)
        txt = res.text
        # print(url)
        soup = BeautifulSoup(txt, 'html.parser')
        divs = soup.find_all('div', {'id': 'paging'})  # 可提取标题
        for d in divs:
            # print(d.form.find_all('a')[-2].text)
            num_of_last_page = d.form.find_all('a')[-2].text
        num_of_last_page = int(num_of_last_page) + 1
        return num_of_last_page

    def get_all_main_page_url(self):
        # 每一个主页的页数
        num_main_page = self.num_main_page

        last_page = self.get_last_page()
        # print('last page: ',last_page)
        while num_main_page < last_page:
            num_main_page += 1
            # print('current num of main page', self.num_main_page)

            # 主页的每一页
            url = self.make_url(num_main_page)
            # print(f'this is page: {num_main_page}: {url}')

            try:
                text = self.get_requests(url)
            except AttributeError:
                print('该视频还未过审核。。。')
                pass
            # print('text: ',text)

            soup = BeautifulSoup(text, 'html.parser')
            divs = soup.find_all('div', {'class': 'well well-sm videos-text-align'})
            # print(divs)
            for index, div in enumerate(divs):
                a_tags = div.find_all('a')
                # print(f'index_of_video: {index}')
                index_of_video = index + 1  # 每个视频的index
                # working_on=len(divs)
                for a_tag in a_tags:
                    # 主页每个视频的子页
                    href = a_tag.get('href')
                    # print(href)

                span_tags = div.find_all('span', {'class', 'video-title title-truncate m-t-5'})
                for span_tag in span_tags:
                    title = span_tag.text  # title
                    # print(f'page:{num_main_page} video:{index_of_video} title:{title} subpage:{href}')

                    self.get_final_data(num_main_page, index_of_video, title, self.get_m3u8(href))

class Crawl:
    def __init__(self):
        self.fhandler = FileHandler()
        self.headers = get_headers()
        self.phandler = PageHandler()
        self.all_links = []

    def crawl(self):
        self.fhandler.mkdir()  # create folder | FileHandler().mkdir()此方法也适用
        # self.fhandler.mkjson()    # create JSON file
        self.phandler.get_all_main_page_url()


Crawl().crawl()
