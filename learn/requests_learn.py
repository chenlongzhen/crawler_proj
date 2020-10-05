import requests, os
import json

#####1. 搜狗搜索#########################
#####1. 搜狗搜索#########################
#####1. 搜狗搜索#########################
url = 'https://www.sogou.com/web?'

# 搜索词参数
kw = input('enter a word')
param = {
    'query': kw
}

# UA伪装
headers = {'User-Agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
response = requests.get(url=url, params=param, headers = headers)

page_text =response.text

os.makedirs('data', exist_ok=True)
fileName = f'data/{kw}.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)

###########post###################
###########post###################
###########post###################

# 1. url post
post_url = 'https://fanyi.baidu.com/sug'

# 2. uA 伪装

# 3. post 请求参数
# 这个是从 network xhr FormData看到的!
kw = input('enter a word')
data = {
    'kw':kw
}

# 4. 发送请求
response = requests.post(url = post_url, data = data, headers=headers)

# 5.获取数据 (如果确认返回时json的才行, content-type中可以看到!)
page_text =response.json()
print(page_text)

# 6. 持久化存储
#json.dump()
#
#os.makedirs('data', exist_ok=True)
#fileName = f'data/{kw}.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    json.dump(page_text, fp = fp, ensure_ascii=False) # ascii 中文


