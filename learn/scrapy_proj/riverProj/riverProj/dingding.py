"""
钉钉通知
"""
import datetime
import json
import requests

def send_dingding_msg(content,
                      robotId = 'd72740c0ea768e4b737da118e6cc8d816e52b03d7626c40aab8193f21730f6f4'):
    try:
        content = f"通知: {content}"
        msg = {
            'msgtype': 'text',
            'text': {'content':
                         content + '\n' + datetime.datetime.now().strftime('%m-%d %H:%M:%S')
                     }
        }

        header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }
        url = 'https://oapi.dingtalk.com/robot/send?access_token='+ robotId
        body = json.dumps(msg)
        msg = requests.post(url, data = body,headers = header)
        print(f"msg: {msg.text}")

    except Exception as err:
        print(f"钉钉发送失败: {err}")
