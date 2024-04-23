import requests
import os
import json
from urllib.parse import urlparse, parse_qs

with open('data.json', 'r') as file:
    json_data = json.load(file)
        # 普通用户
    current_directory = os.getcwd()
print("----------提醒----------")
print("项目地址：https://github.com/JasonYANG170/AutoCheckBJMF")
print("data.json文件位置：", current_directory)
print("----------配置信息(必填)----------")
if (json_data['OFFID1'] == "123"):
    print("请通过查看教程获取URL")
    url = input("请输入粘贴的URL：")
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    OFFID1=""
    OFFID2=""
    if 'sb' in query_params:
        sb_value = query_params['sb'][0]
        sb_parts = sb_value.split('=')  # Split by =

        # 使用正则表达式匹配模式
        # 根据等号分割sb值
        sb_parts = sb_value.split('=')
        # 从切割后的列表中找到不固定的值
        value1 = sb_parts[1] if len(sb_parts) > 1 else None
        value2 = sb_parts[2] if len(sb_parts) > 2 else None
        OFFID1 = value1
        OFFID2 = value2
        print("提取的第一个值:", value1)
        print("提取的第二个值:", value2)
        file_name = "data.json"
        file_path = os.path.join(current_directory, file_name)
        with open(file_path, "r") as file:
            data = json.load(file)

        # 2. 修改数据
        data["OFFID1"] = value1
        data["OFFID2"] = value2
        # 3. 写回JSON文件
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

        print("数据已保存到" + current_directory + "下的data.json中。")
else:
    OFFID1 = json_data['OFFID1']
    OFFID2 = json_data['OFFID2']
#关闭阀门
url = 'http://sdk.xxgcxy.cn/ymcb/gzhnew/stopMeters.action?openid=offline&meterd='+OFFID1+'&meters='+OFFID2+'&price=23.00'  # 替换为你要发送GET请求的URL

response = requests.get(url)
if response.status_code == 200:
    # 请求成功
    data = response.json()  # 获取响应数据
    print(data)
    if(data=="0"):
        print("热水阀门是关闭的，即将执行开启")
    else:
        print("热水阀门正在初始化")
else:
    # 请求失败
    print("请求失败: ", response.status_code)
#开启阀门
url2 = 'http://sdk.xxgcxy.cn/ymcb/gzhnew/startMeters.action?openid=offline&dmeter='+OFFID1+'&smeter='+OFFID2+'&price=23.00&payMoney=330.00&payNumber=1.4347&ts=&rguid='
response2 = requests.get(url2)
if response2.status_code == 200:
    # 请求成功
 #   data2 = response2.json()  # 获取响应数据
    input("请求已经执行，请检查热水阀门是否开启")
else:
    # 请求失败
    print("请求失败: ", response2.status_code)