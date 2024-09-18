import numpy as np

array = np.ones((8, 8))
print('Before:')
print(array)

# Your code goes here
for x in range(1, 7):
    for y in range(1, 7):
        array[x, y] = 0

print('After:') 
print(array)