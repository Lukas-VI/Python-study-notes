import socket
import re
import time

client = socket.socket()
client.connect(("osu.ppy.sh", 80))

data = "GET /users/36996289 HTTP/1.1\r\nHost: osu.ppy.sh\r\nConnection: close\r\n\r\n"
client.send(data.encode())

try:
    first_data = client.recv(4096)
    print("first_data\n", first_data)

    # 检查HTTP状态码
    if b"200 OK" not in first_data:
        print("服务器返回错误：\n", first_data)
        client.close()
        exit(0)

    # 分离头部和内容
    headers, _, body = first_data.partition(b'\r\n\r\n')  # 使用partition分割
    print("Headers:\n", headers)

    # 检查Content-Length
    length_matches = re.findall(b"Content-Length: (\\d+)\n", headers)
    if length_matches:
        length = int(length_matches[0])
        print(f"Content-Length: {length}\n")
        
        # 获取剩余数据
        remaining_data = body
        while len(remaining_data) < length:
            temp = client.recv(4096)
            if not temp:
                break
            remaining_data += temp

    elif b"Transfer-Encoding: chunked" in headers:
        print("使用了chunked传输编码\n")
        # 处理chunked数据的逻辑
        remaining_data = body  # 先获取已接收的内容
        # 继续接收数据直至完整的chunk传输结束...
        while True:
            # 接收chunk长度
            chunk_length_str = client.recv(10).decode()
            if not chunk_length_str:
                break
            chunk_length = int(chunk_length_str, 16)
            # 接收chunk内容
            chunk_data = client.recv(chunk_length)
            # 跳过chunk尾部的\r\n
            client.recv(2)
            # 将chunk内容加入remaining_data
            remaining_data += chunk_data
    else:
        print("未获取到有效的内容长度。\n")

except Exception as e:
    print("发生异常：\n", e)

finally:
    client.close()
