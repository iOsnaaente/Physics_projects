import matplotlib.pyplot as plt 
from math import pi, sin, tan
import numpy as np 


def degree2rad(degree):
    return degree*pi/180

c = 12

a = (c/pi)

Eq1 = lambda x: abs(sin(x))*5 + c 
Eq2 = lambda x: +a*(x) -c
Eq3 = lambda x: -a*(x) +c


intervalo = np.linspace(0, 2*pi, 1000)

Dados_1 = [ [Eq1(y), Eq3(y)] for y in intervalo[:500]]
Dados_2 = [ [Eq1(y), Eq2(y)] for y in intervalo[500:]]

y_val = Dados_1 + Dados_2


for x in intervalo[:500]:
    plt.plot([x,x], [Eq1(x), Eq3(x)], '-')
for x in intervalo[500:]:
    plt.plot([x,x], [Eq1(x), Eq2(x)], '-')


plt.plot(intervalo, y_val, 'o')
plt.subplot(1,1,1)
plt.xlabel('x')
plt.ylabel('eixo')
plt.title('y')
plt.show()





