import requests
import urllib.parse

def login_campus_network(username, password):
    """
    简单的校园网登录函数
    
    Args:
        username (str): 校园网账号
        password (str): 校园网密码
    """
    
    # 从你提供的URL中解析参数
    url = "http://10.101.2.194:6060/portal.do?wlanuserip=10.104.152.78&wlanacname=HSD-BRAS-2&mac=e0:0a:f6:7f:59:0d&vlan=19951084&hostname=LUYH-TB16&rand=de764f4a42773c&url=http%3A%2F%2Fwww.msftconnecttest.com%2Fredirect"
    
    # 解析URL
    parsed_url = urllib.parse.urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
    
    # 解析查询参数
    params = urllib.parse.parse_qs(parsed_url.query)
    
    # 构造登录表单数据
    form_data = {}
    for key, value in params.items():
        form_data[key] = value[0] if isinstance(value, list) else value
    
    # 添加账号密码
    form_data['username'] = username
    form_data['password'] = password
    
    print("登录信息:")
    print(f"  URL: {base_url}")
    print(f"  用户名: {username}")
    print(f"  密码: {'*' * len(password)}")
    print(f"  IP: {form_data.get('wlanuserip')}")
    print(f"  MAC: {form_data.get('mac')}")
    
    try:
        # 发送登录请求
        print("\n正在发送登录请求...")
        response = requests.post(base_url, data=form_data, timeout=10)
        
        print(f"响应状态码: {response.status_code}")
        print(f"响应URL: {response.url}")
        
        # 简单判断登录结果
        if response.status_code == 200:
            content = response.text
            if "成功" in content or "success" in content.lower():
                print("✅ 登录成功!")
            elif "失败" in content or "错误" in content:
                print("❌ 登录失败")
                print("可能的原因:")
                print("  1. 账号或密码错误")
                print("  2. 已经登录")
                print("  3. 网络连接问题")
            else:
                print("⚠️  无法确定登录结果，请手动检查网络连接")
        else:
            print(f"❌ 请求失败 (状态码: {response.status_code})")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ 网络请求错误: {e}")
    except Exception as e:
        print(f"❌ 发生未知错误: {e}")

def main():
    print("校园网登录工具")
    print("=" * 40)
    
    # 输入账号密码
    username = input("请输入校园网账号: ")
    password = input("请输入校园网密码: ")
    
    if not username or not password:
        print("账号或密码不能为空!")
        return
    
    # 执行登录
    login_campus_network(username, password)

if __name__ == "__main__":
    main()