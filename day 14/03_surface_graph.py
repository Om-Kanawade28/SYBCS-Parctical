#surface graph
                         
from mpl_toolkits import mplot3d
                         
import numpy as np
import matplotlib.pyplot as plt
x = np.outer(np.linspace(-2,2,10),np.ones(10))
y = x.copy().T
z = np.cos(x**2 + y**3)
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(x,y,z,cmap='viridis',edgecolor='green')
# <mpl_toolkits.mplot3d.art3d.Poly3DCollection object at 0x000001A25B497B60>

             

ax.set_title('surface plot geeks for geeks')
             
# Text(0.5, 0.92, 'surface plot geeks for geeks')
plt.show()