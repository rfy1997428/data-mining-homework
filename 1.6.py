import numpy as np

filename = 'D:\1\dm\magic04.txt'
aa = np.loadtxt(filename, comments='#', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
b = np.mean(aa, axis=0)
aaa = []
for i in range(0, 10):
    c = np.mat(aa[:, i])
    e = np.var(c)
    aaa.append(e)
max1 = max(aaa)
min1 = min(aaa)
print("方差MAX为：", max1, "方差MIN为：", min1)
