# python2
#coding:utf-8
# Filename: down_movies_name.py
# 获取电影天堂最新电影资源名称，存入 movies_name.txt 内

import re
import requests


user_agent=''
headers={"User-Agent": user_agent}

def get_name():
    url = 'https://www.dytt8.net/'
    data = requests.get(url, headers = headers).content
#    print type(data)
    data1 = data.decode('gbk','ignore').encode('utf-8')
    names = re.findall("最新电影下载</a>]<a href=.+?《(.+?)》", data1, re.S)
    return names

def write_name():
    names = get_name()
    filename = 'movies_name.txt'
    f = open(filename, 'wb')
    for name in names:
        name1 = '《' + name + '》' + '\n'
        f.write(name1)
    f.close()
#    print 'ok'

write_name()
