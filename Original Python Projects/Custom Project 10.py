import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

count = 250
x1 = np.random.rand(count)
y1 = np.random.rand(count)
z1 = 150 -  np.sqrt(x1**2 + y1**2) * np.random.randint(0, 100, count)


colors = 150 - z1
size = 5 *x1 * y1 * z1 + 25
fig  = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.scatter(x1, y1, z1, c = colors, cmap = 'cividis', s = size, alpha = 0.5)


count = 1000
a = np.linspace(0, 1, 20)
b = np.linspace(0, 1, 20)
x2, y2 = np.meshgrid(a, b)
z2 = 150 - 100 * np.sqrt(x2**2 + y2**2)
colors2 = plt.get_cmap('cividis')(np.linspace(0, 1, 20))
#colors2 = plt.cm.cividis(z2)


ax.plot_wireframe(x2, y2, z2, color = colors2, cmap = 'cividis', alpha = 0.5)


x, y = np.random.rand(2, 10000) * 1
hist, xedges, yedges = np.histogram2d(x, y, bins=5, range = [[0, 1], [0, 1]])

xpos, ypos = np.meshgrid(xedges[:-1] + 0.05, yedges[:-1] + 0.05, indexing = 'ij')
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

dx = dy = 0.1 * np.ones_like(zpos)
dz = hist.ravel() * (0.3 - 0.2 * np.sqrt(xpos**2 + ypos**2))

z2 = 150 - 100 * np.sqrt(x2**2 + y2**2)

color = plt.cm.cividis((150 - dz)/max(dz))

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', color = color, cmap = "cividis")
plt.title("Custom Graph 8-2: 3D Bar Chart")

plt.title("Custom Project 10")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()