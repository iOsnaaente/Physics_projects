import matplotlib.pyplot as plt 

import numpy as np 

from algLin import * 

# a titulo de curiosidade, aquele p tem o nome Rho 
raio  = 1 # Fixo / Escala 
phi   = 1 # Azimute
theta = 1 # Zenite    

sin = lambda d : np.sin( np.deg2rad(d) ) 
cos = lambda d : np.cos( np.deg2rad(d) ) 

dom_theta = np.linspace(0, 180 , 9 )
dom_phi   = np.linspace(0, 180 , 18 )

Ps = [ [ raio*sin( p )*cos(t), raio*sin(p)*sin(t), raio*cos(p) ] for p in dom_phi  for t in dom_theta ]


fig = plt.figure()
ax = fig.add_subplot( projection='3d' )

for x, y, z in Ps :
    ax.scatter(x, y, z, marker = 'o', color = 'b' )

plt.show() 