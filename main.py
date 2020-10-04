# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests, parsel , os
from tqdm import tqdm

# 1. 要爬取的网页
url = 'https://mikanani.me/home/classic'
# network 抓包 header
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
response = requests.get(url =url, headers = headers )
print(response)
html_data = response.text

# 2. parse
selector = parsel.Selector(html_data)
url_list = selector.xpath('//tbody/tr/td[3]/a[1]/@href').getall() #xpath 语法

head_url = 'https://mikanani.me'
url_list = [head_url + u for u in url_list]


# 3. 下一页
for u in tqdm(url_list):
    response2 = requests.get(url = u, headers = headers)
    selector2 = parsel.Selector(response2.text)
    title_list = selector2.xpath('//p[@class="episode-title"]/text()').get()
    sourse_list = selector2.xpath('//div[@class="leftbar-nav"]/a[1]/@href').get()
    print(title_list)
    print(sourse_list)

    # 下载种子
    print(f"download torrent: {head_url}{sourse_list}")
    torrent = requests.get(url = f'{head_url}{sourse_list}', headers = headers ).content # 二进制数据

    # 4.数据保存
    os.makedirs('data', exist_ok=True)
    file_name = 'data/' + title_list[:10] + '...'+ title_list[-30:] + '.torrent'
    with open(file_name, mode='wb') as f:
        f.write(torrent)
        print(f"download done. {title_list}")









