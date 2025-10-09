#XPaths:
import requests
import os
from lxml import etree

dirName = '简历模板'
if not os.path.exists(dirName):
    os.mkdir(dirName)

url = 'http://sc.chinaz.com/jianli/free_%d.html'
headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
for page in range(1, 5):
    if page == 1:
        new_url = 'http://sc.chinaz.com/jianli/free.html'
    else:
        new_url = format(url, page)
    r = requests.get(url=new_url, headers=headers)
    r.encoding = r.apparent_encoding
    page_text = r.text
    tree = etree.HTML(page_text)
    a_list = tree.xpath('//div[@id="main"]//div/a')
    for a in a_list:
        title = a.xpath('./img/@alt')[0] + '.zip'
        detail_url = a.xpath('./@href')[0]
        r = requests.get(url=detail_url, headers=headers)
        r.encoding = r.apparent_encoding
        page_text_detail = r.text
        tree = etree.HTML(page_text_detail)
        zip_url = tree.xpath('//ul[@class="clearfix"]/li[4]/a/@href')[0]
        zip_data = requests.get(url=zip_url, headers=headers).content
        zip_path = dirName + '/' + title
        with open(zip_path, 'wb') as fp:
            fp.write(zip_data)
        print(title, '保存成功！')
