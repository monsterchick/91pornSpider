import requests
from bs4 import BeautifulSoup
import ffmpeg, subprocess
import os
import m3u8
import time

all_links = []
page = 0
video_id = 0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Accept-Language': 'zh-TW'}


def make_url(num):
    url = 'https://www.91porn.com/v.php?next=watch&page={}'.format(num)
    return url


def get_ts_list(m3u8_url):
    m3u8_obj = m3u8.load(m3u8_url)
    ts_links = []
    for segment in m3u8_obj.segments:
        ts_links.append(segment.uri)
    # print('ts列表',ts_links)
    return ts_links


def get_last_page():
    res = requests.get(make_url(page), headers=headers)
    txt = res.text
    soup = BeautifulSoup(txt, 'html.parser')
    divs = soup.find_all('div', {'id': 'paging'})  # 可提取标题
    for d in divs:
        # print(d.form.find_all('a')[-2].text)
        num_of_last_page = d.form.find_all('a')[-2].text
    return int(num_of_last_page) + 1


def get_m3u8(suburl):
    res = requests.get(suburl, headers=headers)
    txt = res.text
    soup = BeautifulSoup(txt, 'html.parser')
    id = soup.find('div', {'id': 'VID'}).text
    m3u8_url = f'https://cdn77.91p49.com/m3u8/{id}/{id}.m3u8'
    # print('111',m3u8_url)
    return m3u8_url


def download_video(m3u8_url, title):
    global video_id
    video_id += 1
    # print('标题',title)
    # 解析 M3U8 文件并获取视频片段 URL
    ts_list = get_ts_list(m3u8_url)
    # print('ts列表',ts_list)

    for index, ts in enumerate(ts_list):
        video_url = m3u8_url.rsplit("/", 1)[0] + '/' + ts
        print(f'正在保存第{index}个部分：{video_url}')
        # print(f'正在写入第{index}行',video_url)
        # print('视频的下载链接列表',video_urls)

        # 下载视频片段并保存到本地
        file_path = 'img\\' + str(video_id) + title + '.mp4'
        # print('保存路径',file_path)
        with open(file_path, 'ab') as f:
            res = requests.get(video_url)
            content = res.content
            f.write(content)

def get_all_pagelink(url, page):
    sublink = 0
    res = requests.get(url, headers=headers)
    txt = res.text
    soup = BeautifulSoup(txt, 'html.parser')
    divs = soup.find_all('div', {'class': 'well well-sm videos-text-align'})
    for div in divs:
        # get sublinks
        a_tags = div.find_all('a')
        for a_tag in a_tags:
            href = a_tag.get('href')  # sublink
            # print(f'page:{page} sublink: {sublink} {href}')
            sublink += 1
            get_m3u8(href)
            # print(get_m3u8(href))

        span_tags = div.find_all('span', {'class', 'video-title title-truncate m-t-5'})
        for span_tag in span_tags:
            title = span_tag.text  # title
            # print(f'page:{page} title:{title} sublink: {sublink} {href}')
            print(f'第{page}页 {title}')
            download_video(get_m3u8(href), title)
            print('======================================')
            print('正在爬取第{}页'.format(page), title, href)
            print('======================================')
    print('第{}页爬取完毕\n'.format(page))
    #     break
    # break


last_page = get_last_page()
while page < last_page:
    page += 1
    url = make_url(page)
    # print(f'this is page: {page}: {url}')
    get_all_pagelink(url, page)
    # print(url)
    # print(get_all_pagelink(url))
