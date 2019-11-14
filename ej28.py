import os
import numpy as np
import matplotlib.pyplot as plt


a = os.system("c++ ej28.cpp -o ej28.x")
a = os.system("./ej28.x > ej28.dat")

plt.figure()
data = np.loadtxt("ej28.dat")
plt.plot()

plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("ej28.png")