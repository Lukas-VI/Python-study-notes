import requests
import time

def campus_login(username, password):
    """
    校园网登录函数
    
    Args:
        username (str): 学号或账号
        password (str): 密码
    """
    
    # 构建登录URL（去掉url参数，因为它是重定向目标）
    login_url = "http://10.101.2.194:6060/portal.do"
    
    # 构建POST数据
    payload = {
        'wlanuserip': '10.104.152.78',
        'wlanacname': 'HSD-BRAS-2',
        'mac': 'e0:0a:f6:7f:59:0d',
        'vlan': '19951084',
        'hostname': 'LUYH-TB16',
        'rand': 'de764f4a42773c',
        'username': username,  # 添加用户名
        'password': password   # 添加密码
    }
    
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        # 发送登录请求
        response = requests.post(login_url, data=payload, headers=headers, timeout=10)
        
        # 输出响应信息
        print(f"状态码: {response.status_code}")
        print(f"响应URL: {response.url}")
        
        # 判断登录是否成功（需要根据实际响应调整）
        if response.status_code == 200:
            print("登录请求发送成功")
            if "成功" in response.text or "success" in response.text.lower():
                print("登录成功!")
            else:
                print("登录可能失败，请检查账号密码是否正确")
                # 显示部分响应内容用于调试
                print("响应内容预览:")
                print(response.text[:500] + ("..." if len(response.text) > 500 else ""))
        else:
            print(f"登录失败，错误代码: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
    except Exception as e:
        print(f"发生未知错误: {e}")

def main():
    print("校园网自动登录工具")
    print("=" * 30)
    
    # 在这里填入你的账号和密码
    username = input("请输入账号: ")
    password = input("请输入密码: ")
    
    print("\n正在登录...")
    campus_login(username, password)

if __name__ == "__main__":
    main()