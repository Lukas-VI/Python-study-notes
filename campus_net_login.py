import requests
import urllib.parse
import time
import logging
from typing import Dict, Optional

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CampusNetLogin:
    def __init__(self, username: str, password: str):
        """
        初始化校园网登录器
        
        Args:
            username: 校园网账号
            password: 校园网密码
        """
        self.username = username
        self.password = password
        self.session = requests.Session()
        # 设置请求头，模拟浏览器
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def parse_url_params(self, url: str) -> Dict[str, str]:
        """
        解析URL中的参数
        
        Args:
            url: 包含参数的URL
            
        Returns:
            参数字典
        """
        parsed_url = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed_url.query)
        # 将列表值转换为单个值
        return {k: v[0] if isinstance(v, list) else v for k, v in params.items()}
    
    def login(self, portal_url: str) -> bool:
        """
        执行登录操作
        
        Args:
            portal_url: Portal认证页面URL
            
        Returns:
            登录是否成功
        """
        try:
            # 解析URL参数
            params = self.parse_url_params(portal_url)
            logger.info(f"解析到的参数: {params}")
            
            # 构造登录表单数据
            # 注意：这里需要根据实际的校园网登录页面调整字段名
            login_data = {
                'username': self.username,
                'password': self.password,
                'wlanuserip': params.get('wlanuserip', ''),
                'wlanacname': params.get('wlanacname', ''),
                'mac': params.get('mac', ''),
                'vlan': params.get('vlan', ''),
                'hostname': params.get('hostname', ''),
                'url': params.get('url', '')
            }
            
            # 移除值为空的参数
            login_data = {k: v for k, v in login_data.items() if v}
            
            logger.info("正在尝试登录...")
            
            # 发送登录请求
            # 注意：这里需要根据实际的登录接口URL进行调整
            response = self.session.post(portal_url, data=login_data, timeout=10)
            
            # 检查响应
            if response.status_code == 200:
                logger.info("登录请求发送成功")
                # 这里需要根据实际的登录成功/失败判断逻辑进行调整
                if "登录成功" in response.text or "success" in response.text.lower():
                    logger.info("登录成功!")
                    return True
                else:
                    logger.warning("登录可能失败，请检查响应内容")
                    logger.debug(f"响应内容: {response.text[:500]}...")
                    return False
            else:
                logger.error(f"登录请求失败，状态码: {response.status_code}")
                return False
                
        except Exception as e:
            logger.error(f"登录过程中发生错误: {e}")
            return False
    
    def logout(self, logout_url: str) -> bool:
        """
        执行注销操作
        
        Args:
            logout_url: 注销URL
            
        Returns:
            注销是否成功
        """
        try:
            response = self.session.get(logout_url, timeout=10)
            if response.status_code == 200:
                logger.info("注销请求发送成功")
                return True
            else:
                logger.error(f"注销请求失败，状态码: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"注销过程中发生错误: {e}")
            return False

def main():
    # 配置你的校园网账号信息
    USERNAME = "your_username"
    PASSWORD = "your_password"
    
    # 你提供的URL
    portal_url = "http://10.101.2.194:6060/portal.do?wlanuserip=10.104.152.78&wlanacname=HSD-BRAS-2&mac=e0:0a:f6:7f:59:0d&vlan=19951084&hostname=LUYH-TB16&rand=de764f4a42773c&url=http%3A%2F%2Fwww.msftconnecttest.com%2Fredirect"
    
    # 创建登录器实例
    login_manager = CampusNetLogin(USERNAME, PASSWORD)
    
    # 尝试登录
    if login_manager.login(portal_url):
        logger.info("校园网登录成功")
    else:
        logger.error("校园网登录失败")

if __name__ == "__main__":
    main()