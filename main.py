import requests

#初始化所有response_1
response_1,response_2,response_3,response_4,response_5,response_6,response_7,response_8= None,None,None,None,None,None,None,None
# 第一个目标URL和请求设置
url_base = "https://cyanbug.net/shoutbox.php"

# 请求参数
params_1 = {
    'shbox_text': '青虫娘，求上传',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}

params_2 = {
    'shbox_text': '青虫娘，求魔力',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}
params_5 = {
    'shbox_text': '青虫娘，求彩虹id',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}

params_6 = {
    'shbox_text': '青虫娘，求vip',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}
# 请求头
headers = {
    'Host': 'cyanbug.net',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'iframe',
    'Referer': 'https://cyanbug.net/index.php',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5',
    'Priority': 'u=0, i'
}

# 大青虫Cookies
cookies = {
    'c_secure_uid': '',
    'c_secure_pass': '',
    'c_secure_ssl': '',
    'c_secure_tracker_ssl': '',
    'c_secure_login': ''
}

# 发送第一个GET请求
try:
    response_1 = requests.get(url_base, headers=headers, cookies=cookies, params=params_1)
    print("Response 1:")
    print(response_1.text)
except requests.exceptions.RequestException as e:
    print(f"Error during request 1: {e}")

# 发送第二个GET请求
try:
    response_2 = requests.get(url_base, headers=headers, cookies=cookies, params=params_2)
    print("Response 2:")
    print(response_2.text)
except requests.exceptions.RequestException as e:
    print(f"Error during request 2: {e}")

try:
    response_5 = requests.get(url_base, headers=headers, cookies=cookies, params=params_5)
    print("Response 5:")
    print(response_5.text)
except requests.exceptions.RequestException as e:
    print(f"Error during request 2: {e}")

try:
    response_6 = requests.get(url_base, headers=headers, cookies=cookies, params=params_6)
    print("Response 6:")
    print(response_6.text)
except requests.exceptions.RequestException as e:
    print(f"Error during request 2: {e}")

# tosky 喊
url = "https://t.tosky.club/shoutbox.php"

# 请求参数
params3 = {
    'shbox_text': '来点上传',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}
params4 = {
    'shbox_text': '来点魔力',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}
# 请求头
headers = {
    'Host': 't.tosky.club',
    'Sec-Ch-Ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'iframe',
    'Referer': 'https://t.tosky.club/index.php',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
    'Priority': 'u=0, i'
}

#tosky Cookies
cookies = {
    'c_secure_uid': '',
    'c_secure_pass': '',
    'c_secure_ssl': '',
    'c_secure_tracker_ssl': '',
    'c_secure_login': ''
}

# 发送第三个GET请求
try:
    response_3 = requests.get(url, headers=headers, cookies=cookies, params=params3)
    print("Response 3:")
    print(response_3.text)
except requests.exceptions.RequestException as e:
    print(f"Error during request 3: {e}")

try:
    response_4 = requests.get(url, headers=headers, cookies=cookies, params=params4)
    print("Response 3:")
    print(response_4.text)
except requests.exceptions.RequestException as e:
    print(f"Error during request 3: {e}")

#青蛙喊
url= "https://www.qingwapt.com/shoutbox.php"
params7 = {
    'shbox_text': '蛙总，求上传',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}
params8 = {
    'shbox_text': '蛙总，求下载',
    'shout': '我喊',
    'sent': 'yes',
    'type': 'shoutbox'
}
headers = {
    'Host': 'www.qingwapt.com',
    'Sec-Ch-Ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'iframe',
    'Referer': 'https://www.qingwapt.com/index.php',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
    'Priority': 'u=0, i'
}

#青蛙cookie
cookies = {
    'c_secure_uid': '',
    'c_secure_pass': '',
    'c_secure_ssl': '',
    'c_secure_tracker_ssl': '',
    'c_secure_login': ''
}

try:
    response_7 = requests.get(url, headers=headers, cookies=cookies, params=params7)
    print("Response 7:")
    print(response_7.text)
except requests.exceptions.RequestException as e:
    print(f"Error during request 3: {e}")


#以下为青蛙喊下载，需要请自己删除注释符号
# try:
#     response_8 = requests.get(url, headers=headers, cookies=cookies, params=params8)
#     print("Response 8:")
#     print(response_8.text)
# except requests.exceptions.RequestException as e:
#     print(f"Error during request 3: {e}")



##iyuu自动通知

import requests

# 定义IYUU令牌和API URL
iyuu_key = ""
url = f"https://iyuu.cn/{iyuu_key}.send"



#初始化iyuu返回值
r1, r2, r3, r4, r5, r6, r7, r8 = "", "", "", "", "", "", "", ""
if response_1 is not None and response_1.text.strip():  # strip() 去除前后空白字符
    r1 = "大青虫上传求成功\n"
else:
    r1 = "大青虫求上传失败"
if response_2 is not None and response_2.text.strip():
    r2 = "大青虫魔力求成功\n"
else:
    r2 = "大青虫求魔力失败"
if response_3 is not None and response_3.text.strip():
    r3 = "tosky求上传成功\n"
else:
    r3 = "tosky求上传失败\n"

if response_4 is not None and response_4.text.strip():
    r4 = "tosky求魔力成功\n"
else:
    r3 = "tosky求魔力失败\n"

if response_5 is not None and response_5.text.strip():
    r5 = "大青虫求彩虹ID成功\n"
else:
    r5 = "大青虫求彩虹ID失败\n"
if response_6 is not None and response_6.text.strip():
    r6 = "大青虫求VIP成功\n"
else:
    r6 = "大青虫求VIP失败\n"
if response_7 is not None and response_7.text.strip():
    r7 = "青蛙求上传成功\n"
else:
    r7 = "青蛙求上传失败\n"


if response_8 is not None and response_8.text.strip():

     r8 = "青蛙求下载成功\n"


else:
    r8 = "青蛙求下载失败\n"


# 定义text和desp变量
text = "自动发送get请求"
desp = r1+r2+r3+r4+r5+r6+r7

# 定义请求参数
params = {
    'text': text,
    'desp': desp
}

# 发送GET请求
response = requests.get(url, params=params)

# 打印响应
print("Response Status Code:", response.status_code)
print("Response Text:", response.text)


