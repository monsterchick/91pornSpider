import requests
from bs4 import BeautifulSoup
import m3u8
from make_path import mkdir, mkjson
import os
from avoid_special_characters import avoid_spc_char

from Handle_data import get_last_page, make_url
from Get_all_pagelinks import get_all_pagelink


# dic = {}
all_links = []
page = 0
video_id=0

mkdir()
mkjson()
last_page = get_last_page(page)
while page < last_page:
    page += 1
    # video_id += 1
    url = make_url(page)
    # print(f'this is page: {page}: {url}')
    get_all_pagelink(url, page,video_id)
    # print(url)
    # print(get_all_pagelink(url))
