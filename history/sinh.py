import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
sinh_x = np.sinh(x)
cosh_x = np.cosh(x)
coth_x = np.cosh(x) / np.sinh(x)

plt.figure(figsize=(12, 8))
plt.plot(x, sinh_x, label='双曲正弦 sinh(x)', color='blue')
plt.plot(x, cosh_x, label='双曲余弦 cosh(x)', color='orange')
plt.plot(x, coth_x, label='双曲余切 coth(x)', color='green')

plt.ylim(-10, 10)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.title('双曲函数图像')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
