import numpy as np

#Matrices Con Ones Zeros y Random

#Matriz de Unos (filas x matrices)
unos = np.ones((2,3))

#Matriz de Ceros
ceros = np.zeros((3,4))

#Matriz Random
aleatorio = np.random.default_rng(4).random((5,3,2))

#Matrices con Eyes

x = np.one((2,3))

x.shape = (2, 5)

print(x)