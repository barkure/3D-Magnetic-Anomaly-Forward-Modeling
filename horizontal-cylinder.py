import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置字体为微软雅黑
plt.rcParams['axes.unicode_minus'] = False

# 参数设置
mu_0 = 4*np.pi*10**-7 # 真空磁导率
v = 1000   # 体积
M = 45000 # 磁化强度
m_s = M*v # 磁矩
R = 1000 # 埋深
i_s = np.deg2rad(90) # 有效磁化倾角
I = np.deg2rad(90)  # 磁化倾角

X = np.linspace(-2000, 2000, 101)

# 计算 Z_a, H_a, Delta_T
Z_a = (mu_0 * m_s) / (2 * np.pi * (X**2 + R**2)**2) * ((R**2 - X**2) * np.sin(i_s) - 2 * R * X * np.cos(i_s))

H_a = (mu_0 * m_s) / (2 * np.pi * (X**2 + R**2)**2) * ((R**2 - X**2) * np.cos(i_s) + 2 * R * X * np.sin(i_s))

Delta_T = (mu_0 * m_s) / (2 * np.pi * (X**2 + R**2)**2) * (np.sin(I) / np.sin(i_s)) * ((R**2 - X**2) * np.sin(2 * i_s - np.pi/2) - 2 * R * X * np.cos(2 * i_s - np.pi/2))

# 绘制图形
fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(X, Z_a, label=r'$Z_a$')
ax.plot(X, H_a, label=r'$H_a$')
ax.plot(X, Delta_T, label=r'$\Delta T$')
ax.axhline(0, color='red', linestyle='--')
ax.set_title('水平圆柱体磁异常正演模拟', fontsize=20)
fig.text(0.8, 0.9, f'有效磁化倾角：{i_s/np.pi*180}°', fontsize=13)
ax.set_xlabel('X')
ax.set_ylabel('Value')
ax.legend()

# 保存图像
if not os.path.exists('images'):
    os.makedirs('images')
plt.savefig(f'images/horizontal_cylinder_{i_s/np.pi*180}°.png')

plt.show()

