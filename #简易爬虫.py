#简易爬虫
import socket

# 建立服务器对象      通过打印这个client服务器对象可知：默认使用的是IPV4，协议是TCP。
client=socket.socket()

# 1.建立连接
client.connect(("www.baidu.com",80))

# 构造请求报文
data=b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n"

# 2.发送请求
client.send(data)
res=b""

# 3.接收数据
temp=client.recv(4096)
while temp:
    print("*"*50)
    res += temp
    temp = client.recv(4096)
    print(temp.decode())

# 4.断开连接
client.close()
