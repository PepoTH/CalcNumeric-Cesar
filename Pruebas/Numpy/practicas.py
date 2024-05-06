import numpy as np


matriz = np.random.default_rng().random((3,3))

for i in range(0,len(matriz)):
    for j in range(0,len(matriz[0])):
        matriz[i][j] = np.round(matriz[i][j],3)
        
print(matriz)