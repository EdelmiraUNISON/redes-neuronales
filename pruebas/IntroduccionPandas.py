# Figuras en linea
import matplotlib
%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (15, 5)      # TamaÃ±o de las grÃ¡ficas

matplotlib.style.use('ggplot')

# <---- marca un error relacionado con Date (al quitar esos argumentos, el error desaparece)
#fixed_df = pd.read_csv('bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
fixed_df = pd.read_csv('bikes_2012.csv', sep=';',encoding='latin1', dayfirst=True)
#print(fixed_df[:3])
#fixed_df.describe() #marca un error al ejecutar, se menciona un modo interactivo que hay que prender
#fixed_df['Berri 1'] #<---- marca un error
 
print('finalizado')





