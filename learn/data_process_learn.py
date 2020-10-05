import re, requests, os, parsel
from tqdm import tqdm

if __name__ == "__main__":
    for page_num in range(1,11,1):
        print(f"get page {page_num}")
        url = f'https://www.qiushibaike.com/imgrank/page/{page_num}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

        # 使用通用爬虫对url对应的整个页面爬取
        page_text = requests.get(url=url, headers=headers).text

        # 使用聚焦爬虫,将pic网址爬出
        #
        selector = parsel.Selector(page_text)
        url_list = selector.xpath('//div[2]/a/img/@src').getall()  # xpath 语法
        name_list = selector.xpath('//a/div/span/text()').getall()
        print(len(url_list))
        print(len(name_list))

        save_dir = f'data/xiubaipic/page{page_num}'
        os.makedirs(save_dir, exist_ok=True)
        for n,u in tqdm(zip(name_list, url_list)):
            pic_url = 'https:' + u
            name = n.strip()[:10].replace('/','') +  pic_url[-4:]
            pic_cotent = requests.get(url = pic_url , headers =headers).content
            path = f'{save_dir}/{name}'
            with open(path, 'wb') as fp:
                fp.write(pic_cotent)


