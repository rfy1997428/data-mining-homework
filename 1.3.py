import numpy as np

filename = 'D:\1\dm\magic04.txt'
aaa = np.loadtxt(filename, comments='#', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
bb = np.mean(aaa, axis=0)
c = np.mat(aaa[0])
dd = (c - bb).T*(c - bb)

for i in range(1, aaa.shape[0]):
    c = np.mat(aaa[i])
    dd = dd + (c - bb).T*(c - bb)

print(dd/aaa.shape[0])
