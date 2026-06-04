# 校园网自动登录服务使用说明

## 概述

本项目提供了多种校园网自动登录的解决方案，可以根据需要选择使用。

## 文件说明

1. [campus_net_auto_login.py](file:///d:/py/campus_net_auto_login.py) - 功能完整的自动登录服务，支持定时检查和自动重连
2. [simple_campus_login.py](file:///d:/py/simple_campus_login.py) - 简化版登录脚本，针对特定URL优化
3. [campus_net_login.py](file:///d:/py/campus_net_login.py) - 基础登录框架

## 使用方法

### 方法一：使用简化版登录脚本（推荐新手）

1. 运行 [simple_campus_login.py](file:///d:/py/simple_campus_login.py)：
```bash
python simple_campus_login.py
```

2. 根据提示输入账号和密码

### 方法二：使用完整版自动登录服务

1. 首次运行 [campus_net_auto_login.py](file:///d:/py/campus_net_auto_login.py) 会自动生成配置文件：
```bash
python campus_net_auto_login.py
```

2. 修改生成的 `campus_net_config.json` 文件，填入正确的账号和密码

3. 再次运行程序开始自动登录服务：
```bash
python campus_net_auto_login.py
```

## 配置说明

配置文件 `campus_net_config.json` 包含以下参数：

- `username`: 校园网账号（学号或工号）
- `password`: 校园网密码
- `portal_url`: 认证门户地址
- `check_url`: 网络连接检查地址
- `login_params`: 登录参数
- `interval_minutes`: 自动检查间隔（分钟）

## 注意事项

1. 请确保在连接校园网WiFi或有线网络后再运行登录脚本
2. 不同学校的认证系统可能有所不同，可能需要调整参数名或判断条件
3. 如果登录失败，请检查账号密码是否正确
4. 建议在首次使用时使用 [simple_campus_login.py](file:///d:/py/simple_campus_login.py) 测试账号密码是否有效

## 常见问题

### 1. 登录失败怎么办？

- 检查账号密码是否正确
- 检查网络是否已连接但未认证
- 查看响应内容判断具体错误原因

### 2. 如何判断登录是否成功？

程序会根据响应内容中的关键词判断，如"登录成功"、"success"等。不同学校的系统可能需要调整判断条件。

### 3. 如何停止自动登录服务？

在命令行窗口按 `Ctrl+C` 可以停止自动登录服务。

## 定制开发

如果默认的脚本无法正常工作，可能需要根据实际的认证页面进行调整：

1. 使用浏览器开发者工具查看认证页面的表单字段名
2. 查看实际提交的参数名和URL
3. 根据实际响应内容调整成功/失败判断条件

## 免责声明

本工具仅供学习交流使用，请遵守学校网络使用规定，合理使用网络资源。