# 下载图片并保存到本地
import requests

# 图片 URL
img_url = "https://i02piccdn.sogoucdn.com/a3ffebbb779e0baf"

# 发送请求
response = requests.get(img_url)

# 检查响应状态
if response.status_code == 200:
    # 写入文件
    with open("girl.jpg", "wb") as f:  # 使用 .jpg 扩展名
        f.write(response.content)
        #获取图片的位置
        
    print("图片已成功下载并写入文件{}。".format("f.tell()"))
else:
    print("请求失败，状态码：", response.status_code)
