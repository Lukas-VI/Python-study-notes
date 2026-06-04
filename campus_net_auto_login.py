import requests
import urllib.parse
import time
import json
import logging
from typing import Dict, Optional
import schedule
from datetime import datetime

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CampusNetAutoLogin:
    def __init__(self, config_file: str = "campus_net_config.json"):
        """
        初始化校园网自动登录器
        
        Args:
            config_file: 配置文件路径
        """
        self.config = self.load_config(config_file)
        self.session = requests.Session()
        # 设置请求头，模拟浏览器
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def load_config(self, config_file: str) -> Dict:
        """
        加载配置文件
        
        Args:
            config_file: 配置文件路径
            
        Returns:
            配置字典
        """
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            logger.info("配置文件加载成功")
            return config
        except FileNotFoundError:
            # 如果配置文件不存在，创建一个默认配置文件
            default_config = {
                "username": "your_student_id",
                "password": "your_password",
                "portal_url": "http://10.101.2.194:6060/portal.do",
                "check_url": "http://www.msftconnecttest.com/connecttest",
                "login_params": {
                    "wlanuserip": "10.104.152.78",
                    "wlanacname": "HSD-BRAS-2",
                    "mac": "e0:0a:f6:7f:59:0d",
                    "vlan": "19951084",
                    "hostname": "LUYH-TB16",
                    "rand": "de764f4a42773c",
                    "url": "http://www.msftconnecttest.com/redirect"
                },
                "interval_minutes": 30
            }
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(default_config, f, indent=4, ensure_ascii=False)
            logger.info(f"已创建默认配置文件: {config_file}，请修改其中的账号密码后使用")
            return default_config
        except Exception as e:
            logger.error(f"配置文件加载失败: {e}")
            raise
    
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
    
    def is_logged_in(self) -> bool:
        """
        检查是否已经登录
        
        Returns:
            是否已登录
        """
        try:
            response = self.session.get(self.config['check_url'], timeout=5)
            # 根据实际网络环境调整判断条件
            # 通常未登录时会重定向到认证页面
            if "login" in response.url or "portal" in response.url.lower():
                return False
            return True
        except Exception as e:
            logger.warning(f"网络连接检查失败: {e}")
            return False
    
    def login(self) -> bool:
        """
        执行登录操作
        
        Returns:
            登录是否成功
        """
        try:
            # 构造完整的Portal URL（带参数）
            portal_url = self.config['portal_url']
            login_params = self.config['login_params']
            
            # 发送登录请求
            logger.info("正在尝试登录...")
            response = self.session.post(portal_url, data=login_params, timeout=10)
            
            # 检查响应
            if response.status_code == 200:
                logger.info("登录请求发送成功")
                # 这里需要根据实际的登录成功/失败判断逻辑进行调整
                # 每个学校的认证系统返回格式不同，需要根据实际情况修改判断条件
                if "登录成功" in response.text or "success" in response.text.lower() or "认证成功" in response.text:
                    logger.info("登录成功!")
                    return True
                elif "登录失败" in response.text or "密码错误" in response.text or "账号不存在" in response.text:
                    logger.error("登录失败，账号或密码错误")
                    return False
                else:
                    logger.warning("无法确定登录结果，请检查响应内容")
                    logger.debug(f"响应内容预览: {response.text[:500]}...")
                    # 尝试通过检查网络连接状态判断是否登录成功
                    time.sleep(3)  # 等待认证生效
                    if self.is_logged_in():
                        logger.info("登录成功!")
                        return True
                    else:
                        logger.error("登录可能失败")
                        return False
            else:
                logger.error(f"登录请求失败，状态码: {response.status_code}")
                return False
                
        except Exception as e:
            logger.error(f"登录过程中发生错误: {e}")
            return False
    
    def logout(self) -> bool:
        """
        执行注销操作
        
        Returns:
            注销是否成功
        """
        try:
            # 需要根据实际的注销URL进行调整
            logout_url = self.config['portal_url'].replace('portal.do', 'logout.do')
            response = self.session.get(logout_url, timeout=10)
            if response.status_code == 200:
                logger.info("注销成功")
                return True
            else:
                logger.error(f"注销请求失败，状态码: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"注销过程中发生错误: {e}")
            return False
    
    def auto_login_task(self):
        """
        自动登录任务
        """
        logger.info("执行自动登录检查...")
        if not self.is_logged_in():
            logger.info("检测到未登录，尝试自动登录...")
            if self.login():
                logger.info("自动登录成功")
            else:
                logger.error("自动登录失败")
        else:
            logger.info("网络连接正常，已登录")
    
    def run_scheduler(self):
        """
        运行定时任务调度器
        """
        interval = self.config.get('interval_minutes', 30)
        schedule.every(interval).minutes.do(self.auto_login_task)
        
        logger.info(f"校园网自动登录服务已启动，检查间隔: {interval}分钟")
        logger.info("按 Ctrl+C 停止服务")
        
        # 立即执行一次
        self.auto_login_task()
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("校园网自动登录服务已停止")

def create_config_file():
    """
    创建配置文件示例
    """
    config = {
        "username": "your_student_id",
        "password": "your_password",
        "portal_url": "http://10.101.2.194:6060/portal.do",
        "check_url": "http://www.msftconnecttest.com/connecttest",
        "login_params": {
            "wlanuserip": "10.104.152.78",
            "wlanacname": "HSD-BRAS-2",
            "mac": "e0:0a:f6:7f:59:0d",
            "vlan": "19951084",
            "hostname": "LUYH-TB16",
            "rand": "de764f4a42773c",
            "url": "http://www.msftconnecttest.com/redirect"
        },
        "interval_minutes": 30
    }
    
    with open("campus_net_config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    
    print("配置文件 campus_net_config.json 已创建，请修改其中的账号密码后使用")

def main():
    # 创建登录器实例
    try:
        login_manager = CampusNetAutoLogin()
        
        # 检查是否已正确配置账号信息
        if (login_manager.config['username'] == 'your_student_id' or 
            login_manager.config['password'] == 'your_password'):
            logger.error("请先在 campus_net_config.json 中配置正确的账号和密码")
            return
        
        # 运行定时任务
        login_manager.run_scheduler()
        
    except Exception as e:
        logger.error(f"程序运行出错: {e}")

if __name__ == "__main__":
    main()