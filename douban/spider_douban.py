''' created by xuhong 2018/10/16
完成采集豆瓣图书最受欢迎书评的功能，并对采集到的内容做解析，存储至txt中
采集到的字段包括：用户ID，书评发布时间，书评简介，书评内容，认为有用人数，认为无用人数，回复人数
要采集的网页链接 https://book.douban.com/review/best/
'''

import requests
from lxml import html,etree
import urllib.request
import re

# 获取网页源码
url = 'https://book.douban.com/review/best/'
request_result = requests.get(url)
response_text = request_result.text
request_result = urllib.request.urlopen(url)
# print(request_result)

five_stars_xpath = ".//header[@class='main-hd']/span[@class='allstar50 main-title-rating']/text()"


# 解析网页源码
def parse_(request_result):
    page = html.parse(request_result)
    groups = page.xpath("//div[@class='review-list chart ']/div")
    # print(groups)
    for group in groups:
        print("......")
        name = group.xpath(".//header[@class='main-hd']/a[@class='name']/text()")[0]
        reply = group.xpath(".//div[@class='action']/a[@class='reply']/text()")[0]
        time = group.xpath(".//header[@class='main-hd']/span[@class='main-meta']/text()")[0]
        abstract = group.xpath(".//div[@class='main-bd']/h2/a/text()")[0]
        useful_count = group.xpath(".//div[@class='action']/a[@class='action-btn up']/span/text()")[0].strip()
        useless_count = group.xpath(".//div[@class='action']/a[@class='action-btn down']/span/text()")[0].strip()
        short_content_element = group.xpath(".//div/div[@class='short-content']")
        rc = []
        for node in short_content_element[0].itertext():
            rc.append(node.strip())
        short_content_list = rc
        if len(short_content_list) < 5:
            short_content = short_content_list[0]
        else:
            short_content = short_content_list[2]
        with open('douban.txt','a',encoding='utf8') as f:
            f.write(name+'\t'+time+'\t'+abstract+'\t'+short_content+'\t'+useful_count+'\t'+useless_count+'\t'+reply+'\n')
            print(name)
        # print(short_content)
        # print("name: "+name[0])
        # print("time: "+time[0])
        # print("abstract: "+abstract[0])
        # print("short_content: "+)
        # print("useful_count: "+useful_count[0].strip())
        # print("useless_count: "+useless_count[0].strip())
        # print("reply: "+reply[0])
        # print("star: "+star)
parse_(request_result)

def get_short_content(response_text):
    pattern = '<div class="short-content">.*(?=&nbsp)'
    print(response_text)
    response_text = re.sub("\n", "--", response_text)
    # print(response_text)
    short_contents = re.search(pattern, response_text)
    print(short_contents.group())
# get_short_content(response_text)


# 获取下一页的link
def get_next_page(text):
    pass

#print(response_text)
# response_text = """<div id="review_9593753_short" class="review-short" data-rid="9593753">
#                     <div class="short-content">
#                             <p class="spoiler-tip">这篇书评可能有关键情节透露</p>

#                         在前一段时间，我看到好多友邻都在探讨国内外名著的“三观”问题，当我看到这一话题时，第一个反应就是《简·爱》这部小说肯定会中枪，点开相关的帖子和话题一看，《简·爱》的“三观”讨论果然名列前茅。 比如“绿茶女主套路渣男一般的高帅富男主”、“原配家属大闹小三和渣男...

#                         &nbsp;(<a href="javascript:;" id="toggle-9593753-copy" class="unfold" title="展开">展开</a>)
#                     </div>"""
# response_text.replace('\n', '==')
# response_text = re.sub("\n", "--", response_text)

# pattern1 = re.findall('<p class="spoiler-tip">这篇书评可能有关键情节透露</p>(.*?)&nbsp', response_text)
# pattern2 = re.findall('<p class="spoiler-tip">这篇书评可能有关键情节透露</p>(.*?)&nbsp', response_text)
# print(pattern1, len(pattern1))