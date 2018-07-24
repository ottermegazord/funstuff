import matplotlib.pyplot as plt
import numpy as np
import csv

fname = 'test.csv'

r = np.genfromtxt(fname, delimiter=',')
print(r[:,1])

plt.figure()
plt.plot(r[:,0], r[:,1])
plt.show()

p