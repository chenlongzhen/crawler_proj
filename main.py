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

os.makedirs('data', exist_ok=True)
magnet_filename = 'data/magnet.txt'
with open(magnet_filename, mode='w') as mf:

    # 3. 进入下一页获取磁力链接和种子并存储
    for u in tqdm(url_list):
        try:
            response2 = requests.get(url = u, headers = headers)
            selector2 = parsel.Selector(response2.text)
            # 这里使用xpath进行路径匹配 使用chrome的xpath helper工具即可
            title = selector2.xpath('//p[@class="episode-title"]/text()').get()
            source = selector2.xpath('//div[@class="leftbar-nav"]/a[1]/@href').get()
            magnet = selector2.xpath('//div[@class="leftbar-nav"]/a[2]/@href').get()
            print(title)
            print(source)
            print(magnet)


            # 下载种子
            print(f"download torrent: {head_url}{source}")
            torrent = requests.get(url = f'{head_url}{source}', headers = headers ).content # 二进制数据

            # 4.数据保存
            mf.write(f"{title}\t{magnet}\n")

            file_name = 'data/' + title[:10] + '...'+ title[-30:] + '.torrent'
            with open(file_name, mode='wb') as f:
                f.write(torrent)
                print(f"download done. {title}")
        except Exception as e:
            print(f"err: {e}")
            continue









