# 三国小说爬取
# https://www.shicimingju.com/book/sanguoyanyi.html

import re, requests, os, parsel
from tqdm import tqdm
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    # 使用通用爬虫对url对应的整个页面爬取
    page_text = requests.get(url=url, headers=headers).text

    # 实例化
    soup = BeautifulSoup(page_text, 'lxml')
    # 解析
    li_list = soup.select('.book-mulu > ul > li')  # 层级解析

    with open('./data/sanguo.txt', 'w') as fp:
        for li in li_list:
            title = li.a.string
            detail_url = 'http://www.shicimingju.com' + li.a['href']
            detail_page_text = requests.get(detail_url, headers=headers).text
            detail_soup = BeautifulSoup(detail_page_text, 'lxml')

            # 取文章内容
            div_tag = detail_soup.find('div', class_='chapter_content')
            content = div_tag.text.strip()
            fp.write(title+':' + content + '\n')
            print(f'title: {title} finish.')
