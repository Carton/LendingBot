# coding=utf-8
# Desc: 测试Bitfinex API

import requests
import json

url = "https://api.bitfinex.com/v1/lendbook/USD?limit_asks=0&limit_bids=5"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

# 解析响应文本为Python对象
data = json.loads(response.text)

# 使用json.dumps函数并设置indent参数来格式化输出
pretty_data = json.dumps(data, indent=4, ensure_ascii=False)

print(pretty_data)