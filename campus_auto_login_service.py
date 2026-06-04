import requests
import time
import json
import os
import sys
import argparse
from datetime import datetime

class CampusNetworkLogin:
    def __init__(self, config_path="campus_config.json"):
        self.config_path = config_path
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
        self.load_config()
    
    def load_config(self):
        """加载配置文件"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            # 默认配置
            self.config = {
                "username": "",
                "password": "",
                "portal_url": "http://10.101.2.194:6060/portal.do",
                "login_params": {
                    "wlanuserip": "10.104.152.78",
                    "wlanacname": "HSD-BRAS-2",
                    "mac": "e0:0a:f6:7f:59:0d",
                    "vlan": "19951084",
                    "hostname": "LUYH-TB16",
                    "rand": "de764f4a42773c",
                    "url": "http://www.msftconnecttest.com/redirect"
                },
                "check_urls": [
                    "http://www.msftconnecttest.com/connecttest",
                    "http://www.baidu.com"
                ]
            }
            self.save_config()
            print(f"已创建配置文件: {self.config_path}，请填写账号密码后使用")
    
    def save_config(self):
        """保存配置文件"""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)
    
    def update_credentials(self, username, password):
        """更新账号密码"""
        self.config["username"] = username
        self.config["password"] = password
        self.save_config()
        print("账号密码已更新")
    
    def is_connected(self):
        """检查网络连接状态"""
        # 首先检查是否能访问网络
        try:
            # 尝试访问微软的网络连接测试端点
            response = self.session.get("http://www.msftconnecttest.com/connecttest", timeout=5)
            
            # 如果返回200且内容包含"Microsoft Connect Test"，说明已通过认证
            if response.status_code == 200 and "Microsoft Connect Test" in response.text:
                return True
            
            # 如果重定向到认证页面或其他内容，说明未通过认证
            return False
        except:
            # 如果完全无法访问，则说明没有网络连接
            return False
    
    def login(self):
        """执行登录操作"""
        if not self.config["username"] or not self.config["password"]:
            print("错误: 请先设置账号密码")
            return False
        
        # 构造登录数据，使用正确的参数格式
        login_data = self.config["login_params"].copy()
        login_data["userid"] = self.config["username"]  # 使用 userid 而不是 username
        login_data["passwd"] = self.config["password"]  # 使用 passwd 而不是 password
        
        # 构造正确的登录URL
        login_url = self.config["portal_url"].replace("portal.do", "quickauth.do")
        
        print(f"使用登录URL: {login_url}")
        print(f"登录参数: {login_data}")
        
        try:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 正在登录...")
            response = self.session.post(login_url, data=login_data, timeout=10)
            
            print(f"登录响应状态码: {response.status_code}")
            content_preview = response.text[:500] if len(response.text) > 500 else response.text
            print(f"登录响应内容前{len(content_preview)}字符:\n{content_preview}")
            
            if response.status_code == 200:
                content = response.text
                
                # 检查各种可能的成功标识
                success_indicators = ["success", "认证成功", "登陆成功", "登录成功", "welcome", "欢迎", '"result":"success"']
                failure_indicators = ["密码错误", "账号不存在", "失败", "error", "incorrect", "无效", "不正确", '"result":"fail"']
                
                if any(indicator in content for indicator in success_indicators):
                    print("✅ 登录成功!")
                    return True
                elif any(indicator in content for indicator in failure_indicators):
                    print("❌ 登录失败，请检查账号密码")
                    return False
                else:
                    print("⚠️  登录完成，但无法确认结果，请手动验证网络连接")
                    # 检查是否能访问外网来判断是否登录成功
                    if self.is_connected():
                        print("✅ 通过网络连接测试确认登录成功")
                        return True
                    else:
                        print("❌ 通过网络连接测试确认登录失败")
                        return False
            else:
                print(f"❌ 登录请求失败 (状态码: {response.status_code})")
                return False
                
        except Exception as e:
            print(f"❌ 登录过程中发生错误: {e}")
            return False
    
    def logout(self):
        """执行注销操作"""
        try:
            logout_url = self.config["portal_url"].replace("portal.do", "logout.do")
            response = self.session.get(logout_url, timeout=10)
            if response.status_code == 200:
                print("✅ 注销成功")
                return True
            else:
                print(f"❌ 注销失败 (状态码: {response.status_code})")
                return False
        except Exception as e:
            print(f"❌ 注销过程中发生错误: {e}")
            return False
    
    def auto_login(self, interval=30):
        """自动登录服务"""
        print(f"🚀 启动自动登录服务 (检查间隔: {interval}分钟)")
        print("按 Ctrl+C 停止服务")
        
        # 立即检查一次
        self.check_and_login()
        
        while True:
            try:
                time.sleep(interval * 60)  # 转换为秒
                self.check_and_login()
            except KeyboardInterrupt:
                print("\n👋 自动登录服务已停止")
                break
    
    def check_and_login(self):
        """检查连接状态并登录（如果需要）"""
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 检查网络连接...")
        if not self.is_connected():
            print("🌐 检测到网络未连接或未通过认证，尝试登录...")
            self.login()
        else:
            print("✅ 网络连接正常且已通过认证")

def main():
    parser = argparse.ArgumentParser(description='校园网自动登录工具')
    parser.add_argument('-u', '--username', help='校园网账号')
    parser.add_argument('-p', '--password', help='校园网密码')
    parser.add_argument('-i', '--interval', type=int, default=30, help='检查间隔(分钟)，默认30分钟')
    parser.add_argument('--login', action='store_true', help='执行一次登录')
    parser.add_argument('--logout', action='store_true', help='执行注销')
    parser.add_argument('--auto', action='store_true', help='启动自动登录服务')
    
    args = parser.parse_args()
    
    # 创建登录实例
    login_service = CampusNetworkLogin()
    
    # 更新账号密码（如果提供）
    if args.username and args.password:
        login_service.update_credentials(args.username, args.password)
    
    # 执行相应操作
    if args.login:
        login_service.login()
    elif args.logout:
        login_service.logout()
    elif args.auto:
        login_service.auto_login(args.interval)
    else:
        # 默认行为：检查并登录
        login_service.check_and_login()

if __name__ == "__main__":
    main()