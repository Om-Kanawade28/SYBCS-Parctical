from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')
z = np.linspace(0,1,100)
x = z*np.sin(25*z)
y = z*np.cos(25*z)
c = x + y
ax.scatter(x,y,z,c = c)
# <mpl_toolkits.mplot3d.art3d.Path3DCollection object at 0x0000020F02125520>
ax.set_title('3D Scatter plot geeks gor geeks')
# Text(0.5, 0.92, '3D Scatter plot geeks gor geeks')
plt.show()