import numpy as np
import matplotlib.pyplot as plt
import math
filename = 'D:\1\dm\magic04.txt'

aa = np.loadtxt(filename, comments='#', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
c1 = np.mat(aa[:, 0])
s = np.mean(c1.T, axis=0)
dd = []
dd = s.getA()
dd = dd[0][0]
d2 = np.var(c1, axis=1)
bzc = math.sqrt(d2)
print(dd, "  ", bzc)

x = np.linspace(dd - 3*bzc, dd + 3*bzc, 50)
y = np.exp(-(x - dd) ** 2 / (2 * bzc ** 2))/(math.sqrt(2*math.pi)*bzc)
plt.plot(x, y, "r-", linewidth=2)
plt.grid(True)
plt.show()
