import numpy as np 

A = np.array([
    [1, 4, 4],
    [2, 3, 2],
    [7, 6, 7]
])

B = np.array([
    [8, 1, 0],
    [6, 3, 2],
    [5, 6, 7]
])

resultado = np.dot(A,B)

print ("resultado de matriz:")
print (resultado)