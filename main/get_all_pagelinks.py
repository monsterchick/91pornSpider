import requests
from bs4 import BeautifulSoup
from handle_data.headers import headers
from handle_data.handle import HandleData
from save.download_sources import download_videos


handle_data = HandleData()

def get_pagelinks(first_url, page_num):
    print(first_url,page_num)

    try:
        res = requests.get(first_url, headers=headers)
    except AttributeError:
        print('该视频还未过审核。。。')
        pass
    txt = res.text
    soup = BeautifulSoup(txt, 'html.parser')
    divs = soup.find_all('div', {'class': 'well well-sm videos-text-align'})
    for div in divs:
        a_tags = div.find_all('a')
        for a_tag in a_tags:

            # each url includes a video
            second_page = a_tag.get('href')
            # print(1,second_page)

        span_tags = div.find_all('span', {'class', 'video-title title-truncate m-t-5'})
        for span_tag in span_tags:

            # the title to extract
            title = span_tag.text
            print(title, second_page)
            download_videos(handle_data.get_m3u8(second_page), title, page_num)

    print('第{}页爬取完毕\n'.format(page_num))

class UrlsCollector:
    def __init__(self):
        self.page = 0
        self.first_urls = []

    def get_first_urls(self):
        page = self.page
        first_urls = self.first_urls

        # the number of last page
        last_page = handle_data.get_last_page(page)
        while page < last_page:
            page += 1

            # each url that contains sub pages
            first_url = handle_data.make_url(page)
            first_urls.append(first_url)

        # a list of all first urls
        return first_urls
    def get_second_urls(self):
        # current page of number
        page_num = self.page

        # a list of first urls
        first_urls = self.first_urls
        # print(first_urls)
        for first_url in first_urls:
            page_num += 1
            # print(first_url)
            # print(page_num)
            get_pagelinks(first_url,page_num)





