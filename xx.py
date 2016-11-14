#!/usr/bin/env python
import re
import requests
import random
import sys
from time import sleep
f = open('film.txt','a')
#25662330开始
print(sys.getdefaultencoding())
for i in range(26670898,27000000):
    html = requests.get('https://movie.douban.com/subject/'+str(i)+'/')
    html.encoding = 'utf-8'

    patt = re.compile('<span property="v:itemreviewed">(.*?)</span>')
    tagpat = re.compile('<a href="/tag/(.*?)" class="">')

    name = re.findall(patt,html.text)
    tags = re.findall(tagpat,html.text)
    print(i)
    for each in name:
        f.write('\n'+each+' ')
        print(each)
        '''
        try:
            print(each)
        except:
            break
        '''

    for each in tags:
        f.write(','+each)
    sleep(random.uniform(1,2))      #睡眠函数用于防止爬取过快被封IP

f.close()
#快捷回复给：刘立琛
