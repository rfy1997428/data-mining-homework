import numpy as np

filename = 'D:\1\dm\magic04.txt'
aaa = np.loadtxt(filename, comments='#', delimiter=',', usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
bbb = np.mean(aaa, axis=0)
print(bbb)
