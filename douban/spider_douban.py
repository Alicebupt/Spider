''' created by xuhong 2018/10/16
完成采集豆瓣图书最受欢迎书评的功能，并对采集到的内容做解析，存储至txt中
采集到的字段包括：用户ID，书评发布时间，书评简介，书评内容，认为有用人数，认为无用人数，回复人数
要采集的网页链接 https://book.douban.com/review/best/
'''

import requests
from lxml import html,etree
import urllib.request
import re

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
# parse_(request_result)

# 使用正则表达式解析网页源码
def regex_parse(response_text):
    '''
    对一个网页进行解析，提取其中有用信息并写入result.txt
    Args:
        response_text: str, 网页源码
    '''
    response_text = re.sub("\n", "--", response_text)
    response_text = response_text.split('<div xmlns:v=')
    del response_text[0]
    for text in response_text:
        book_name = re.findall('<img alt="(.*?)"',text)[0].strip()
        name = re.findall('class="name">(.*?)</a>', text)[0].strip()
        time = re.findall('class="main-meta">(.*?)</span>', text)[0].strip()
        try:
            star = re.findall('<span property="v:rating" class="allstar(.*?)main', text)[0].strip()
            star = int(star)/10
        except:
            star = 0
        review = re.findall('<h2><a(.*?)</a>', text)[0].strip().split('>')[1]
        reply = re.findall('class="reply">(.*?)回应</a>', text)[0].strip()
        try:
            tip = re.findall('<p class="spoiler-tip">(.*?)</p>', text)[0].strip()
            content = re.findall('<p class="spoiler-tip">这篇书评可能有关键情节透露</p>(.*?)&nbsp', text)[0].strip('- ')
        except:
            tip = ''
            content = re.findall('<div class="short-content">(.*?)&nbsp', text)[0].strip('- ')
        with open('./douban/regex_result.txt', 'a', encoding='utf8') as f:
            f.write(book_name+'\t'+name+'\t'+time+'\t'+str(star)+'\t'+review+'\t'+tip+'\t'+content+'\t'+reply+'\n')

# 获取下一页的link
def get_next_page(text):
    base_url = 'https://book.douban.com{}'
    url = re.findall('<link rel="next" href="(.*?)"/>', text)[0]
    next_page_url = base_url.format(url)
    return next_page_url

next_page = 'https://book.douban.com/review/best/'

while next_page:
    # 获取网页源码
    request_result = requests.get(next_page)
    response_text = request_result.text
    # 对当前页进行解析
    regex_parse(response_text)
    # 获取下一页的链接
    try:
        next_page = get_next_page(response_text)
    except:
        break
    print(next_page)
