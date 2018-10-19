# created by xuhong 2018/10/16
# 完成采集豆瓣图书散文类的图书信息的功能，并对采集到的内容做解析，存储至txt中
# 要采集的网页链接 https://book.douban.com/tag/%E7%AB%A5%E8%AF%9D

import requests
from lxml import html,etree
import urllib.request
from bs4 import BeautifulSoup
import re

# 获取网页源码
url = 'https://book.douban.com/review/best/'
# request_result = requests.get(url)
# response_text = request_result.text
# print(type(response_text))
request_result = urllib.request.urlopen(url)
print(request_result)

five_stars_xpath = ".//header[@class='main-hd']/span[@class='allstar50 main-title-rating']/text()"


# 解析网页源码
page = html.parse(request_result)
groups = page.xpath("//div[@class='review-list chart ']/div")
print(groups)
for group in groups:
    print("......")
    name = group.xpath(".//header[@class='main-hd']/a[@class='name']/text()")
    reply = group.xpath(".//div[@class='action']/a[@class='reply']/text()")
    time = group.xpath(".//header[@class='main-hd']/span[@class='main-meta']/text()")
    abstract = group.xpath(".//div[@class='main-bd']/h2/a/text()")
    short_content = group.xpath(".//div/div[@class='short-content']/text()")   
    useful_count = group.xpath(".//div[@class='action']/a[@class='action-btn up']/span/text()")
    useless_count = group.xpath(".//div[@class='action']/a[@class='action-btn down']/span/text()")
    star = group.xpath(five_stars_xpath)
    print(star)
    print("name: "+name[0])
    print("time: "+time[0])
    print("abstract: "+abstract[0])
    print("short_content: "+short_content[0].strip())
    print("useful_count: "+useful_count[0].strip())
    print("useless_count: "+useless_count[0].strip())
    print("reply: "+reply[0])
    # print("star: "+star)

def get_short_content(response_text):
    pattern = '<div class="short-content">(.*)?&nbsp;'



# 获取下一页的link
def get_next_page(text):
    pass