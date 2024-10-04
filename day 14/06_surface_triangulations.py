from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')
n = 10
theta = np.linspace(-4*np.pi,4*np.pi,n)
z = np.linspace(-2,2,n)
r = z**2 + 1
x = r*np.cos(theta)
y = r*np.sin(theta)
ax.plot_trisurf(x,y,z,cmap='viridis',edgecolor='green')
# <mpl_toolkits.mplot3d.art3d.Poly3DCollection object at 0x0000020F02125520>
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('surface triangulation geeks for geeks')
# Text(0.5, 0.92, 'surface triangulation geeks for geeks')
plt.show()
             