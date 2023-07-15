from make_path import mkdir
from handle_data.handle import HandleData
from get_all_pagelinks import get_pagelinks
from get_all_pagelinks import UrlsCollector
from handle_data.handle import HandleData

# first_page_list = []
page = 0
video_id=0

# handle_data = HandleData()
collector = UrlsCollector()
handle = HandleData()

# make a folder called "download" if it does not exist
mkdir()

# the number of last page
# last_page = handle_data.get_last_page(page)
# print(last_page)

# while page < last_page:
#     page += 1
#
#     # each url that contains sub pages
#     first_url = handle_data.make_url(page)
#     print(first_url)

    # get_pagelinks(first_url, page)
collector.get_first_urls()
collector.get_second_urls()
# get_video_url(second_urls)
