import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))


x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = f(x, y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot')

plt.show()