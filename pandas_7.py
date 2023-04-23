import json

import pandas as pd

obj = """{
    "name":"Wes",
    "places_lived":["US","Spain","Germany"],
    "pet":null,
    "siblings":[{"name":"Scott","age":30,"pets":
                 ["Zeus","Zuko"]},
                {"name":"Katie","age":38,
                 "pets":["Sixes","Stache","Cisco"]}]
}"""
# 利用loads方法将json字符串转换为Python形式
result = json.loads(obj)
print(result)
# print(result['siblings'][0]['pets'])
# 利用dumps方法将Python对象转换为JSON字符串
asjson = json.dumps(result)
# print(asjson)
siblings = pd.DataFrame(result['siblings'],columns=['name','age'])
print(siblings)
# read_json自动将JSON数据集按照指定次序转换为Series和DataFrame
data = pd.read_json('json_1.json')
print(data)
# 如果将pandas数据导出为JSON，
# 可以利用Series和DataFrame中的to_json
print(data.to_json())
