import requests
from bs4 import BeautifulSoup
import m3u8
from Headers import headers

def make_url(num):
    url = 'https://www.91porn.com/v.php?next=watch&page={}'.format(num)
    return url


def get_last_page(page):
    res = requests.get(make_url(page), headers=headers)
    txt = res.text
    soup = BeautifulSoup(txt, 'html.parser')
    divs = soup.find_all('div', {'id': 'paging'})  # 可提取标题
    for d in divs:
        # print(d.form.find_all('a')[-2].text)
        num_of_last_page = d.form.find_all('a')[-2].text
    return int(num_of_last_page) + 1


def get_ts_list(m3u8_url):
    m3u8_obj = m3u8.load(m3u8_url)
    ts_links = []
    for segment in m3u8_obj.segments:
        ts_links.append(segment.uri)
    # print('ts列表',ts_links)
    return ts_links

def get_m3u8(suburl):
    res = requests.get(suburl, headers=headers)
    txt = res.text
    soup = BeautifulSoup(txt, 'html.parser')
    id = soup.find('div', {'id': 'VID'}).text
    m3u8_url = f'https://cdn77.91p49.com/m3u8/{id}/{id}.m3u8'
    ts_list = get_ts_list(m3u8_url)
    # print('test sublink',suburl)
    return ts_list, m3u8_url, suburl
