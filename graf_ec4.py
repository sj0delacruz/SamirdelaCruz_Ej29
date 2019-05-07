import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm

seleccion = np.loadtxt("dat_ec4.dat")

fig = plt.figure(figsize=(15,7))

ax = fig.add_subplot(1,2,1,projection='3d')
xx, yy = np.mgrid[0:seleccion.shape[0], 0:seleccion.shape[1]]
ax.plot_surface(xx/50, yy/100, seleccion ,rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)


plt.ylabel("Posicion [metros]")
plt.xlabel("Tiempo [segundos]")

cueer = np.loadtxt("dat_ec4.dat")
x=np.linspace(0,1,cueer.shape[1])


ax = fig.add_subplot(1,2,2)
plt.plot(x,cueer[0],label="Tiempo inicial")
plt.plot(x,cueer[-1],label="Tiempo final")
plt.legend()
plt.xlabel("Posicion [metros]")
plt.ylabel("Desplazamiento [metros]")

plt.savefig("graf_ec4.png")