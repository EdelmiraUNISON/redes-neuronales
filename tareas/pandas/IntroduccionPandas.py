# Figuras en linea
import matplotlib
#%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (15, 5)      # Tamaño de las gráficas

matplotlib.style.use('ggplot')

broken_df = pd.read_csv('bikes.csv')

print('finalizado')

# Vamos a ver las 3 primeras entradas
broken_df[:3]



