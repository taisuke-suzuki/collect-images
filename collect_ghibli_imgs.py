# coding: utf-8

import requests
import bs4
import os
import time

# 各作品の画像ページへのリンクの取得

res = requests.get('https://www.ghibli.jp/works/')
soup = bs4.BeautifulSoup(res.content,'html.parser')
urls=soup.select('.btn')
work_tags=[]
for i in urls:
    if i.getText() == '作品静止画':
        work_tags.append(i)
work_urls=[]
for i in work_tags:
    work_urls.append(i.get('href'))
time.sleep(5)

# 全ての作品名の取得とフォルダの作成

title_tags = soup.select('.post-header')
titles=[]
for i in title_tags:
    if i.find('span',itemprop='name'):
        title=i.find('span',itemprop='name')
        titles.append(title.text)
for i in titles:
    os.mkdir(i)


# 対象作品の画像を各フォルダに格納する

work_title_no = 0
work_img_no =1
for i in work_urls:
    res = requests.get(i)
    soup = bs4.BeautifulSoup(res.content,'html.parser')
    imgs=soup.select('.panel-img-top')
    img_urls=[]
    for j in imgs:
        img_urls.append(j.get('src'))
    time.sleep(5)

    for j in img_urls:
        res = requests.get(j)
        with open(titles[work_title_no]+'/'+titles[work_title_no].strip()+str(work_img_no)+str('.jpeg'),'wb')as file:
            file.write(res.content)
            work_img +=1
        time.sleep(2)
    work_img_no=1
    work_title_no+=1
    time.sleep(3)
