import nmap

def perform_ip_scan(target):
    # 创建Nmap对象
    nm = nmap.nmap

    # 扫描目标IP地址范围
    nm.scan(target, arguments='-sP -O -T4 -p 80-1023 '+ 'and '.join(map(str, range(192, 193))))

    # 获取扫描结果
    scan_result = nm.response()

    # 输出扫描结果
    for host in scan_result.hosts():
        print('Host: %s' % host.address)
        print('State: %s' % host.state())
        print('Open ports: %s' % host.open_ports())

# 将目标IP地址替换为你想要扫描的IP地址范围
target_ip_range = '192.168.31.0/24'
perform_ip_scan(target_ip_range)