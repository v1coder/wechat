# python2
# -*- coding: utf-8 -*-
# Filename: download_qiushibaike.py
"""
下载糗事百科 24h hot 里的段子，存到本地 qiushibaike.txt ，过滤掉“图片”和“查看全文”
"""

import requests
import re

user_agent = ''
headers = {'User-Agent':user_agent}

# 读取网页上的数据
def download_data(url):
    url = url
    data = requests.get(url, headers = headers).content
    return data

# 用正则得到正文数据，返回列表
def get_text(data):
    data = data
    text_list = re.findall('<div class="content">(.+?)</span>', data, re.S)
    return text_list

# 去掉数据中的空格、<p>、</p>
def remove_str(text):
    text = text
    # 去掉 <p>、</p>
    text1 = re.sub('<.+?>', '', text)
    # 去掉空格和空行
    text2 = text1.replace(" ", "").replace('\n', '')
    return text2
    
# 把数据写入文档
def write_text(text_list):
    text_list = text_list
    filename = 'qiushibaike.txt'
    f = open(filename, 'wb')
    for text in text_list:
        text1 = remove_str(text)
        text2 = text1 + '\n'
        # 去掉过短的（一般是图片）和过长的（查看全文）段子
        if len(text2) > 111 and len(text2) < 600:
            f.write(text2)
    f.close()
    
def start(url):
    url = url
    data = download_data(url)
    text_list = get_text(data)
    write_text(text_list)
    
url = 'https://www.qiushibaike.com/hot/'
start(url)
#print 'ok'
