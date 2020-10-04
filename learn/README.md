# 爬虫学习
https://www.bilibili.com/video/BV1Yh411o7Sz?p=2

## 1. 分类
1. 通用爬虫： 一整张页面数据
2. 聚焦爬虫：特定局部内容
3. 增量爬虫：检测数据更新，只抓取更新出来的数据

## 2. robots.txt 协议
 规定那些可以以及不能爬取。 https://www.taobao.com/robots.txt

## 3.1 http
- 概念：服务器和客户端进行数据交互的一种形式。

### 常用请求头信息
- User-Agent: 请求载体的身份信息
    - chrome network 中能够获取
- Connection: 请求完毕后，是断开还是保持连接

### 常用响应头信息
- Content-Type: 服务器端响应回服务器端的数据类型

## 3.2 https
- 概念: 安全的超文本传输协议

### 加密方式
- 对称加密
- 非对称加密
- 证书加密

## 4 requests模块
网络请求模块, 模拟浏览器发请求

流程:
- 指定url
- 发起请求 get post
- 获取相应数据
- 持久化存储相应数据

### 4.1 UA伪装
让爬虫对应的请求伪装成浏览器, 在chrome里network扎到user-agent即可
```python
# UA伪装
headers = {'User-Agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
response = requests.get(url=url, params=param, headers = headers)
```

## 4.2 post请求
```
https://fanyi.baidu.com/#zh/en/%E7%8B%97
network-xhr-选择相应post结果-response里是结果
Request URL: https://fanyi.baidu.com/sug
Request Method: POST
content-type: application/json
Form Data:  kw:gou (输入的是狗)
```

post请求携带了参数,携带了json数据,如何发post请求?
```python
w = input('enter a word')
data = {
    'kw':kw
}

# 4. 发送请求
response = requests.post(url = post_url, data = data, headers=headers)

# 5.获取数据 (如果确认返回时json的才行, content-type中可以看到!)
page_text =response.json()
```

## 4.3 

 


