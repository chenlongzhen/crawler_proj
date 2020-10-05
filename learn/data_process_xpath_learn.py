# 二手房房源信息
# https://www.shicimingju.com/book/sanguoyanyi.html

import  requests,os
from lxml import etree

if __name__ == "__main__":
    url = 'https://bj.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    # 使用通用爬虫对url对应的整个页面爬取
    page_text = requests.get(url=url, headers=headers).text

    # 实例化
    tree = etree.HTML(page_text)
    #r = tree.xpath('/html/body/div[5]/div[5]/div[1]/ul/li')
    r = tree.xpath('//ul[@class="house-list-wrap"]/li')

    file_dir = 'data/58data'
    os.makedirs(file_dir, exist_ok=True)
    with open(file_dir+'/58.txt', 'w') as fp:
        for li in r:
            text = li.xpath('./div[2]/h2/a/text()')[0]
            price = li.xpath('./div[3]/p[1]/b/text()')[0]
            print(text)
            print(price)
            fp.write(f"{text}\t{price}\n")

