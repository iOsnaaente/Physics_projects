from matplotlib.animation import FuncAnimation

import matplotlib.pyplot as plt 
import numpy as np 
import algLin

num_frames = 180
theta = np.linspace( 0, 2*np.pi, 50 ) 
raio  = 10

# definição dos limites de plotagem 
fig, ax = plt.subplots(figsize=(5, 3))

ax.set(xlim=(-raio*1.5, raio*1.5), ylim=(-raio*1.5, raio*1.5))


# Pontos usados para desenhar a geometria
# Z é usado somente para manter os 3 eixos
P = [ [np.cos(ang), np.sin(ang), 0] for ang in theta]


def animate( i ): 
    p = P_animation[i]
    scat.set_offsets( np.c_[p[0], p[1]] ) 

P_animation = [] 

for frame in range( num_frames ): 
    # para girar o circulo, vamos chamar a função ROT_X 
    P_rot_x = [ np.array([x,y,z,0]).dot( algLin.Rot_X( np.deg2rad(frame) )).dot( algLin.Rot_Y( np.deg2rad(frame))).dot( algLin.Rot_Z( np.deg2rad(frame) ) )[:2] for x, y, z in P  ] 
    x = [ val[0]*raio for val in P_rot_x  ]
    y = [ val[1]*raio for val in P_rot_x  ]
    P_animation.append( [x,y] )


scat = ax.scatter(P_animation[0][0], P_animation[0][1] ) 
anim = FuncAnimation( fig, animate, interval = 1, frames= 180 )

plt.draw() 
plt.show() 