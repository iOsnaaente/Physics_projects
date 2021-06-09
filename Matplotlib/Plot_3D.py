from matplotlib.ticker import LinearLocator, FormatStrFormatter 
from matplotlib import pyplot as plt, cm
from mpl_toolkits.mplot3d import Axes3D

import numpy as np 


imc = lambda p, h : p / (h**2)      

peso   = np.linspace(31, 100, 100)
altura = np.linspace(1, 2, 100)


IMC  = imc ( peso, altura )
peso, altura = np.meshgrid(peso, altura) 

fig = plt.figure()
ax  = fig.gca( projection = '3d' ) 

scale = 8 


# Calculo da altura do homem 
surf = ax.plot_surface( peso, altura, IMC, cmap = cm.coolwarm, linewidth = 0, antialiased = False )

for angle in range(0, 360):
    ax.view_init(30,40)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)


plt.show()

