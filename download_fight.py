# python2
# -*- coding: utf-8 -*-
# Filename: download_fight.py
"""
下载简书里的素材到本地文档 fight.txt
"""

import requests
import re

user_agent = ''
headers = {'User-Agent':user_agent}

# 读取网页上的数据
def download_fight(url):
    url = url
    data = requests.get(url, headers = headers).content
    return data

# 用正则得到正文数据，返回列表
def get_text(data):
    data = data
    text_list = re.findall('<div class="show-content-free">(.+?)</div>', data, re.S)
    return text_list

# 去掉数据中的空格、<p>、</p>
def remove_str(text):
    text = text
    # 去掉 <p>、</p>
    text1 = re.sub('<.+?>', '', text)
    # 去掉空格和空行
    text2 = text1.replace(" ", "")
    return text2
    
# 把数据写入文档
def write_text(text_list):
    text_list = text_list
    filename = 'fight.txt'
    f = open(filename, 'wb')
    for text in text_list:
        text1 = remove_str(text)
        f.write(text1)
    f.close()
    
def start(url):
    url = url
    data = download_fight(url)
    text_list = get_text(data)
    write_text(text_list)
    
url = 'https://www.jianshu.com/p/713415f82576'
start(url)
#print 'ok'
