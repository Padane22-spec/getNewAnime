'''
Author: padane22 461834180@qq.com
Date: 2022-11-17 21:49:26
LastEditors: padane22 461834180@qq.com
LastEditTime: 2022-11-17 21:50:42
FilePath: \getNewAnime\anime.py
Description: 

Copyright (c) 2022 by padane22 461834180@qq.com, All Rights Reserved. 
'''
import requests
from bs4 import BeautifulSoup

def main():
    webSite = 'https://anime1.me'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.2.760634598.1610870362; __cfduid=d96d70942d1f45247029bf1f14aea03971614588585; _gid=GA1.2.494659697.1614588586'
    }

    # 服务器返回响应
    r = requests.get(webSite, headers=headers)
    demo = r.text

    soup = BeautifulSoup(demo, "html.parser",)

    s_body = soup.tbody
    s_trs = s_body.find_all('tr')

    my_f = open('./source/anime.txt', 'w',encoding='gb18030')
    for tr in s_trs[:20]:
        tds = tr.contents
        name = tds[0].text
        href = tds[0].a.get('href')
        number = tds[1].text
        print(name, '\t',number, '\t',webSite+href)
        my_f.write(name)
        my_f.write('\t')
        my_f.write(number)
        my_f.write('\n')
    my_f.close()
    # print(s_body)

if __name__ == '__main__':
    main()