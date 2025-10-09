import requests as r 

import numpy as np  # noqa: F401
import matplotlib.pyplot as plt # noqa: F401
from matplotlib import font_manager
from sympy import content

# 设置字体
font_path = 'C:/Windows/Fonts/simhei.ttf'  # 根据你的系统字体路径进行修改
font_prop = font_manager.FontProperties(fname=font_path)

#下载个人档案https://osu.ppy.sh/users/36996289，找到osu!记录，复制列表数据到list变量中

def get_Response(url):
    try: 
        res = r.get(url,timeout=30,headers=HEADER)
        res.encoding = res.apparent_encoding
        res.raise_for_status()
        return res.text
    except(r.ConnectionError):
        print("Error: 无法连接到服务器")
        return "404"
    except(r.Timeout):
        print("Error: 请求超时")
        return "Timeout"
    except(r.HTTPError):
        print("Error: HTTP 错误")
        return "ErrorHTTP"
    except(r.TooManyRedirects):
        print("Error: 重定向过多")
        return "TMR"
    except(r.URLRequired):
        print("Error: 需要URL")
        return "urlRequired"
    except(r.ConnectTimeout):
        print("Error: 连接超时")
        return "ConnectTimeout"

'''

get构造向服务器请求资源的request对象，并将返回的response对象赋值给r变量
request(
    url, 
    method='GET'/POST/PUT/DELETE/PATCH/HEAD, 
    params=None, 
    data=None, 
    headers=None, 
    cookies=None, 
    files=None, 
    auth=None, 
    timeout=None, 
    allow_redirects=True, 
    proxies=None, 
    hooks=None, 
    stream=None, 
    verify=None, 
    cert=None, 
    json=None)
'''
#**kwargs表示可变参数，可以传入任意数量的键值对，这些键值对会被作为参数传递给函数。

HEADER={'user-agent':'Mozila/5.0'}

url = 'https://osu.ppy.sh/users/36996289'

def search_playerurl(mode:str,content:str):
    url = "None"
    if mode == "ID":
        url = 'https://osu.ppy.sh/users/' + content
    elif mode == "Name":
        kv={'mode':'user','query':content}
        res = r.get('https://osu.ppy.sh/home/search',params=kv,headers=HEADER)
        print(res.url)
        print(res.status_code)
        if res.status_code == 200:
            try:
                url = res.url
            except(Exception):
                print("Error: 未找到该玩家")
                return "Error"
            print(res.text)
    else:
        print("Error: 请输入正确的模式")
        return "Error"
    return url

def get_player_res(url):
    if url == "Error":
        print("Error: 请输入正确的玩家ID或用户名")
        return "Error"
    res = get_Response(url)
    print(r.status_codes)
    return res

#def get_player_cover(res):

#print(r.content)二进制数据

'''
#解析列表数据
#列表格式是[排名，排名，排名，...]其中0代表没有排名
list = [2479681,2211410,2091354,1914714,1692987,1635697,1638552,1565625,1550103,1552256,1554394,1462842,1465090,1362489,1364515,1331738,1312643,1284007,1272895,1262108,1250199,1251851,1253384,1254921,1256389,1218261,1219704,1220488,1204504,1171674,1168244,1164604,1165928,1150610,1120395,1121341,1120593,1093997,1095331,1096590,1091043,1092297,1093567,1094921,1096084,1085049,1069364]

#把列表数据转换为csv格式，并保存到本地
np.savetxt('osu!.csv', list, delimiter=',', fmt='%d')

#读取csv文件
data = np.loadtxt('osu!.csv', delimiter=',', dtype=int)

#画图
plt.plot(data)
plt.title('osu!排名变化图'   , fontproperties=font_prop)
plt.xlabel('时间'           , fontproperties=font_prop)
plt.ylabel('排名'           , fontproperties=font_prop)
plt.show()

'''

if __name__ == '__main__':
    content=input("请输入玩家ID或用户名：")
    mode=input("请输入模式（ID/Name）：")
    url=search_playerurl(mode,content)
    res = get_player_res(url)
    print(res)
    # 解析列表数据
