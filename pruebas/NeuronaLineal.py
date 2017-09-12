def mse_loss(x, y, w):
    """
    Calcula el costo de acuerdo al criterio de MSE (mean square error) asumiendo un conjunto de datos
    x, con una salida y, y una hipótesis lineal parametrizada por omega
    
    @param x: Un ndarray de dimension (T, n + 1)
    @param y: Un ndarray de dimensión (T, 1)
    @param w: Un ndarray de dimensión (n + 1, 1)
    
    @return: Un número real con el costo
    """
    T, n = x.shape[0], x.shape[1] - 1
    
    # Puedes hacerlo en forma de ciclos
    #J = 0
    #for instancia in range(T):
    #    J += ((x[instancia].dot(w)-y[instancia])**2)/(2*T)        
    #return J
    
    # Puedes hacerlo directamente en forma matricial 
    error = (x.dot(w)-y)**2
    return np.sum(error)/(2*T)
#########################################################################

import numpy as np
import matplotlib.pyplot as plt

# Lee los datos en un nd array llamado datos
datos = np.loadtxt('datos/carretas.txt', comments='%', delimiter=',')

# Separa los datos de entrada de los de salida.
# si decimos que x = datos[:,0], pues se toma solo una columna de datos,
# por lo que x sería un ndarray de forma (shape) (96,). Al decir x = datos[:, 0:1] 
# significa que vamos a tomar todas las columnas de 0 a una antes de 1, por lo
# que x tiene una forma (96, 1). Para nuestros intereses, es mejor manejar x xomo una matriz
# de una sola columna que como un vector de una dimensión (igual para y).
x, y = datos[:,0:1], datos[:,1:] 

# T es el número de instancias y n el de atributos
T, n = x.shape
print(T,n)
plt.plot(x, y, 'rx')
plt.title(u'Ganancias anuales de una carreta de acuerdo al tamaño de una ciudad')
plt.xlabel(r"Poblaci$\'o$n ($\times 10^4$ habitantes)")
plt.ylabel(r'Beneficios ($\times 10^4$ dolares)')
    
x = np.c_[np.ones_like(x), x]
print(x.shape[0],x.shape[1])
    
