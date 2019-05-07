import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm

seleccion = np.loadtxt("dat_ec4.dat")

fig = plt.figure()

ax = Axes3D(fig)
xx, yy = np.mgrid[0:seleccion.shape[0], 0:seleccion.shape[1]]
ax.plot_surface(xx/50, yy/100, seleccion ,rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)


plt.ylabel("Posicion [metros]")
plt.xlabel("Tiempo [segundos]")


plt.savefig("graf_ec4(1).png")