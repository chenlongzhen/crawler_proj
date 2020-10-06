import asyncio
import time

async def request(url):
    print(f'download', url)
    # 在异步携程中如果出现了同步模块的代码, 那么就无法实现异步!!!!!!!!!
    # time.sleep(2)
    # 遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print(f'finish', url)

start = time.time()
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.gounamjia.com'
]

stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(stasks))#!!!!!!!

print(time.time() - start)
