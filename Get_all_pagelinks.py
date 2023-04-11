import requests
from bs4 import BeautifulSoup
from Headers import headers
from Handle_data import get_m3u8
from download_sources import download_videos


working_on = 0
def get_all_pagelink(url, page,video_id):
    sublink = 0

    try:
        res = requests.get(url, headers=headers)
    except AttributeError:
        print('该视频还未过审核。。。')
        pass
    txt = res.text
    soup = BeautifulSoup(txt, 'html.parser')
    divs = soup.find_all('div', {'class': 'well well-sm videos-text-align'})
    for div in divs:
        # get sublinks    # 用于调试
        a_tags = div.find_all('a')


        # working_on=len(divs)
        for a_tag in a_tags:

            href = a_tag.get('href')  # sublink
            # print(f'page:{page} sublink: {sublink} {href}')
            sublink += 1
            # get_m3u8(href)
            ts_list = get_m3u8(href)
            # print(ts_list)


        span_tags = div.find_all('span', {'class', 'video-title title-truncate m-t-5'})
        for span_tag in span_tags:

            title = span_tag.text  # title
            # print(f'page:{page} title:{title} sublink: {sublink} {href}')
            global working_on
            working_on += 1
            download_videos(get_m3u8(href), title,video_id, page,working_on,url)
    working_on=0
    print('第{}页爬取完毕\n'.format(page))
