import numpy as np
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

theta0 = np.linspace(0,np.pi/2, 100)
theta1 = np.linspace(0,np.pi/2, 100)
theta2,theta3 = np.meshgrid(theta0,theta1)

r = 5
x = np.cos(theta3)*np.sin(theta2) * r
y = np.sin(theta3)*np.sin(theta2) * r
z = np.cos(theta2)* r

fig = plt.figure()
ax = fig.add_subplot(100,projection = "3d")
ax.plot_surface(x,y,z)
plt.xlim([0,3])
plt.xlim([3,0])
ax.set_zlim([0,3])
plt.xlabel("X")
plt.xlabel("Y")
plt.xlabel("Z")
plt.show()


