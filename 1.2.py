import numpy as np

filename = 'D:\1\dm\magic04.txt'
a = np.loadtxt(filename, comments='#', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
b = np.mean(a, axis=0)
c = a - 1*b.T
dd = np.mat(c)
ee = dd.shape[0]

gg = (dd.T*dd)*(1/ee)
print(gg)
