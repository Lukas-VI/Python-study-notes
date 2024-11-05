import numpy as np
import matplotlib.pyplot as plt
import control

# 定义PID参数
Kp_values = [0.5, 1.0, 1.5]  # 不同的比例增益
Ki = 0.1  # 积分增益
Kd = 0.05 # 微分增益

# 定义时间范围和阶跃输入
t = np.linspace(0, 10, 500)  # 0到10秒，500个样本
u = np.ones_like(t)          # 单位阶跃输入

plt.figure()

# 为每个Kp值绘制响应曲线
for Kp in Kp_values:
    # 创建PID控制器传递函数
    num = [Kd, Kp, Ki]  # PID的传递函数分子
    den = [1, 0, 0]     # 传递函数分母
    pid = control.TransferFunction(num, den)
    
    # 计算PID控制器的响应
    t_out, y_out = control.forced_response(pid, T=t, U=u)
    
    # 绘制响应曲线
    plt.plot(t_out, y_out, label=f'Kp = {Kp}')

# 完善图像
plt.title('PID Controller Response')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.axhline(y=1, color='r', linestyle='--', label='Setpoint')  # 目标值线
plt.grid()
plt.legend()  # 添加图例
plt.show()
