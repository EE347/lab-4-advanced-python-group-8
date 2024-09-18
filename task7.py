import numpy as np


x = np.linspace(0, 10, 101)
cosx = np.cos(x)
sinx = np.sin(x)
np.save("task7_sin.npy", sinx)
np.save("task7_cos.npy", cosx)