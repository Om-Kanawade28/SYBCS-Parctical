#Wireframes
             
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
ax.plot_wireframe(X,Y,Z,color='green')
# <mpl_toolkits.mplot3d.art3d.Line3DCollection object at 0x000002F267F155B0>

ax.set_title('wireframe geeks for geeks')
             
# Text(0.5, 0.92, 'wireframe geeks for geeks')
plt.show()