import numpy as np
import matplotlib.pyplot as plt
sinfile = np.load('task7_sin.npy')
cosfile = np.load('task7_cos.npy')
x = np.linspace(0, 10, 101)
plt.plot(x, sinfile, x, cosfile)
plt.legend(['sin(x)', 'cos(x)'])
plt.show()