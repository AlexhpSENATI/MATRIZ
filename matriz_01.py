import numpy as np 

matriz = np.array ([
    [1, 4, 4],
    [2, 3, 2],
    [7, 6, 7],
    [8, 7, 8]  
])

matriz_final = np.delete(matriz, 2, axis=1 )

print(matriz_final) 