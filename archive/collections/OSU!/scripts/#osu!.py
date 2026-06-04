#osu查分
import re  # noqa: F401
import os  # noqa: F401

import requests as r 
from bs4 import BeautifulSoup as bs  # noqa: F401
from lxml import etree   # noqa: F401
import numpy as np  # noqa: F401
import matplotlib.pyplot as plt # noqa: F401
from matplotlib import font_manager

# 设置字体
font_path = 'C:/Windows/Fonts/simhei.ttf'  # 根据你的系统字体路径进行修改
font_prop = font_manager.FontProperties(fname=font_path)

#下载个人档案https://osu.ppy.sh/users/36996289，找到osu!记录，复制列表数据到list变量中

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

HEADER={'User-Agent':'Mozila/5.0'}
url = 'https://osu.ppy.sh/users/36996289'

class Get():
    def __init__(self):
        pass
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

    def search_url(mode:str,contentstr:str):
        url = "None"
        if mode == "ID":
            url = 'https://osu.ppy.sh/users/' + contentstr
        '''
        elif mode == "Name"(abandoned):
            kv={'mode':'user','query':contentstr}
            res = r.get('https://osu.ppy.sh/home/search',params=kv,headers=HEADER,stream=True,)
            print(res.url)
            #tree = etree.HTML(res.text)
            #url = tree.xpath('//a[@class="user-card__username u-ellipsis-pre-overflow"]')
            #print(url)
            try:
                soup = bs(res.text, 'html.parser')
                root = "D:/py/OSU!/test"
                path = os.path.join(root, "de.txt")
                if not os.path.exists(root):
                    os.makedirs(root)
                if not os.path.exists(path):
                    print("正在保存页面数据...")
                    with open(path, "wb") as f:
                        f.write(res.content)
                    print("保存成功")
            except Exception as e:
                print(f"Error: 页面数据保存失败, {e}")


            url = soup.find_all('a',class_='user-card__username u-ellipsis-pre-overflow')
            print(url)
            #/html/body/div[7]/form/div[2]/div[3]/div[1]/div/div/div/div/a

        else:
            print("Error: 请输入正确的模式")
            return "Error"'''
        
        return url

    def get_res(url):
        if url == "Error":
            print("Error: 请输入正确的玩家ID或用户名")
            return "Error"
        res = Get.get_Response(url)
        print(r.status_codes)
        return res

    def decode_res(res):
        soup = bs(res, 'html.parser')
        return soup
    
    def get_cover(url):
        id = 0000
        url = "https://assets.ppy.sh/user-cover-presets/15/8ddd8423001f11dc5b57508720413b22001a0f62acb91cea14219f27fab481f5.png"
        root = "./temp/{}".format(id)
        path = root + "/{}cover.jpg".format(id)
        try:
            if not os.path.exists(root):
                os.makedirs(root)
            if not os.path.exists(path):
                print("正在获取封面图片...")              
                res = r.request("GET",url)
                print(res.status_code)
                with open(path,"wb") as f:
                    f.write(res.content)
                print("封面图片保存成功")
                f.close()
                return path
            else:
                print("封面图片已存在")
        except(r.exceptions.RequestException):
                print("Error: 封面图片获取失败")
                return "Error"
        
    def get_score(soup):
        score = ""
        try:
            score = soup.find_all('meta', attrs={'name': 'description'})
        except Exception as e:
            print(f"Error: 解析失败, {e}")
        return score



class Player():
    def __init__(self,soup,cover,name,id,Globle_rank_list,Contry_rank_list,score):
        self.soup = None
        self.cover = None
        self.name = None
        self.id = None
        self.Globle_rank_list = None
        self.Contry_rank_list = None
        self.score = None
    def get_url(self):
        pass

#print(r.content)二进制数据
'''
print(type(r))
print(r.headers)
print(r.encoding)           #从headers中获取编码方式
print(r.apparent_encoding)  #从内容中分析出编码方式

'''



if __name__ == '__main__':
    
    #解析列表数据
    #列表格式是[排名，排名，排名，...]其中0代表没有排名
    list = [2479681,2211410,2091354,1914714,1692987,1635697,1638552,1565625,1550103,1552256,1554394,1462842,1465090,1362489,1364515,1331738,1312643,1284007,1272895,1262108,1250199,1251851,1253384,1254921,1256389,1218261,1219704,1220488,1204504,1171674,1168244,1164604,1165928,1150610,1120395,1121341,1120593,1093997,1095331,1096590,1091043,1092297,1093567,1094921,1096084,1085049,1069364]

    #把列表数据转换为csv格式，并保存到本地
    np.savetxt('osu!.csv', list, delimiter=',', fmt='%d')

    #读取csv文件
    data = np.loadtxt('osu!.csv', delimiter=',', dtype=int)

    #画图
    plt.plot(data)
    plt.title('osu!排名变化图'      , fontproperties=font_prop)
    plt.xlabel('时间'              , fontproperties=font_prop)
    plt.ylabel('排名'              , fontproperties=font_prop)
    plt.show()


    #contentstr = input("请输入玩家ID：")
    contentstr = "37027657"
    mode = "ID"
    player = Player(None,None,None,None,None,None,None)
    url = Get.search_url(mode,contentstr)
    print(url)
    res = Get.get_res(url)
    player.soup = Get.decode_res(res)
    player.score = Get.get_score(player.soup)
    print(player.score)
    #print(Get.decode_res(res))
    #Get.get_cover(url)
    # 解析列表数据

    # 解析个人信息