from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return np.sin(np.sqrt(x**2 + y**2))

x = np.linspace(-1,5,10)
y = np.linspace(-1,5,10)
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X,Y,Z,50,cmap='viridis')
# <mpl_toolkits.mplot3d.art3d.Line3DCollection object at 0x0000020F02125520>
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('contour 3D geeks for geeks')
# Text(0.5, 0.92, 'contour 3D geeks for geeks')
plt.show()
