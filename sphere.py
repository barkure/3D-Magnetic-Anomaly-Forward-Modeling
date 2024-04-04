import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import webbrowser
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置字体为微软雅黑
plt.rcParams['axes.unicode_minus'] = False

# 参数设置
mu_0 = 4*np.pi*10**-7 # 真空磁导率
v = 1000   # 体积
M = 45000 # 磁化强度
m = M*v # 磁矩
R = 1000 # 埋深

X, Y = np.meshgrid(np.linspace(-R, R, 51), np.linspace(-R, R, 51))

fig = plt.figure(figsize=(10, 10))
fig.suptitle('球体磁异常正演模拟', fontsize=20)
ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222, projection='3d')
ax3 = fig.add_subplot(223, projection='3d')
ax4 = fig.add_subplot(224, projection='3d')
I_label = fig.text(0.81, 0.91, '', fontsize=15)

def update(i):
    I = np.deg2rad(i)  # 将角度转换为弧度
    A_prime = np.deg2rad(0)  # 将角度转换为弧度

    # 计算H_ax, H_ay, Z_a, Delta_T
    H_ax = (mu_0 / (4*np.pi)) * (m / (X**2 + Y**2 + R**2)**(5/2)) * \
    ((2*X**2 - Y**2 - R**2) * np.cos(I) * np.cos(A_prime) - 3*R*X * np.sin(I) + 3*X*Y * np.cos(A_prime) * np.sin(I))

    H_ay = (mu_0 / (4*np.pi)) * (m / (X**2 + Y**2 + R**2)**(5/2)) * \
        ((2*Y**2 - X**2 - R**2) * np.cos(I) * np.cos(A_prime) - 3*R*Y * np.sin(I) + 3*X*Y * np.cos(A_prime) * np.sin(I))

    Z_a = (mu_0 / (4*np.pi)) * (m / (X**2 + Y**2 + R**2)**(5/2)) * \
        ((2*R**2 - X**2 - Y**2) * np.sin(I) - 3*R*X * np.cos(I) * np.cos(A_prime) - 3*R*Y * np.cos(I) * np.sin(A_prime))

    Delta_T = (mu_0 / (4*np.pi)) * (m / ((X**2 + Y**2 + R**2)**(5/2))) * \
        ((2*R**2 - X**2 - Y**2) * np.sin(I)**2 + (2*X**2 - Y**2 - R**2) * np.cos(I)**2 * np.cos(A_prime)**2 + \
        (2*Y**2 - X**2 - R**2) * np.cos(I)**2 * np.sin(A_prime)**2 - 3*X*R * np.sin(2*I) * np.cos(A_prime) + \
        3*X*Y * np.cos(I)**2 * np.sin(2*A_prime) - 3*Y*R * np.sin(2*I) * np.sin(A_prime))

    # 清除之前的图形
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()

    # 重新绘制图形
    ax1.plot_surface(X, Y, H_ax, cmap='viridis', edgecolor='none')
    ax1.set_title(r'$H_{ax}$')  # 设置标题
    ax1.set_xlabel('X')  # 设置x轴标签
    ax1.set_ylabel('Y')  # 设置y轴标签
    ax1.set_zlabel(r'$H_{ax}$')  # 设置z轴标签

    ax2.plot_surface(X, Y, H_ay, cmap='viridis', edgecolor='none')
    ax2.set_title(r'$H_{ay}$')  # 设置标题
    ax2.set_xlabel('X')  # 设置x轴标签
    ax2.set_ylabel('Y')  # 设置y轴标签
    ax2.set_zlabel(r'$H_{ay}$')  # 设置z轴标签

    ax3.plot_surface(X, Y, Z_a, cmap='viridis', edgecolor='none')
    ax3.set_title(r'$Z_{a}$')  # 设置标题
    ax3.set_xlabel('X')  # 设置x轴标签
    ax3.set_ylabel('Y')  # 设置y轴标签
    ax3.set_zlabel(r'$Z_{a}$')  # 设置z轴标签

    ax4.plot_surface(X, Y, Delta_T, cmap='viridis', edgecolor='none')
    ax4.set_title(r'$\Delta T$')  # 设置标题
    ax4.set_xlabel('X')  # 设置x轴标签
    ax4.set_ylabel('Y')  # 设置y轴标签
    ax4.set_zlabel(r'$\Delta T$')  # 设置z轴标签

    # 更新文本标签显示当前角度
    I_label.set_text(f'磁化倾角 I = {i}°')

# 创建动画
ani = FuncAnimation(fig, update, frames=range(0, 91), interval=50)
print('正在生成动画，请稍等...')
ani.save('sphere.gif', writer='pillow')

# 播放GIF
print('正在播放动画...')
# 获取当前工作目录
cwd = os.getcwd()
# GIF的文件名
gif_filename = "sphere.gif"
# 创建GIF的完整路径
gif_path = os.path.join(cwd, gif_filename)
# 在默认的web浏览器中打开GIF
webbrowser.open(gif_path)
