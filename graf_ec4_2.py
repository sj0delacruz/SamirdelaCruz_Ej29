import numpy as np
import matplotlib.pyplot as plt

cueer = np.loadtxt("dat_ec4.dat")
x=np.linspace(0,1,cueer.shape[1])

plt.figure(figsize=(5,5))
plt.plot(x,cueer[0],label="Tiempo inicial")
plt.plot(x,cueer[-1],label="Tiempo final")
plt.legend()
plt.xlabel("Posicion [metros]")
plt.ylabel("Desplazamiento [metros]")
plt.savefig("graf_ec4(2).png")