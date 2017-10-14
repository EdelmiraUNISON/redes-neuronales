# Neurona lineal (notebook de redes neuronales)#
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from feedforward import *

#bloque 2

# Lee los datos en un nd array llamado datos
#datos = np.loadtxt('datos/carretas.txt', comments='%', delimiter=',')
datos = pd.read_csv('datos/CHR-1.csv',sep=',',header = 1)
print('Tipo de dato = ',type(datos))

numMuestras,numAtributos = datos.shape

print('Numero de muestras =',numMuestras)
print('Numero de atributos= ',numAtributos)


#SetPrueba = datos[2:40,:]

#SetTest = datos[41:56,4:]
#print('setPrueba.shape =',setPrueba.shape)

