from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')
z = np.linspace(0,1,100)
x = z*np.sin(25*z)
y = z*np.cos(25*z)
ax.plot3D(x,y,z,'green')
# [<mpl_toolkits.mplot3d.art3d.Line3D object at 0x000002253F0E1A60>]
ax.set_title('3 D lin plot geeks for geeks')
# Text(0.5, 0.92, '3 D lin plot geeks for geeks')
plt.show()