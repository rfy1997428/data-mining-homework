import numpy as np

filename = 'D:\1\dm\magic04.txt'
aaa = np.loadtxt(filename, comments='#', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
bbb = np.mean(aaa, axis=0)
cc = []
g = []

for i in range(0, 10):
    for j in range(i+1, 10):
        c1 = np.mat(aaa[:, i])
        c2 = np.mat(aaa[:, j])
        e = np.cov(c1, c2)
        g = e
        cc.append(g[0][1])

max1 = max(cc)
min1 = min(cc)

print("协方差MAX：", max1, "协方差MINE：", min1)

