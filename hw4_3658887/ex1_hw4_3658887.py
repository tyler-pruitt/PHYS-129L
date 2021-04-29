#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 06:06:13 2020

@author: tylerpruitt
"""


import numpy as np
import matplotlib.pyplot as plt

def dist_cubed(x,y):
    return abs((x**2 + y**2)**(3/2))

def dist_squared(x,y):
    return abs(x**2 + y**2)

def dist(x,y):
    return abs((x**2 + y**2)**(1/2))

x_0 = float(input('Enter initial x positon at t=0: '))
y_0 = float(input('Enter initial y positon at t=0: '))
X_0 = (x_0, y_0)

vx_0 = float(input('Enter initial x velocity at t=0: '))
vy_0 = float(input('Enter initial y velocity at t=0: '))
V_0 = (vx_0, vy_0)

t_0 = 0
dt = float(input('Enter time interval: '))
Ttot = float(input('Enter total runtime: '))

steps = int(Ttot/dt)
print('steps:', steps)

x, y, vx, vy, t = [x_0], [y_0], [vx_0], [vy_0], [t_0]

vx_0 -= (x_0 / dist_cubed(x_0,y_0))*dt/2
vy_0 -= (y_0 / dist_cubed(x_0,y_0))*dt/2

for i in range(steps):
    x_0 += vx_0*dt
    y_0 += vy_0*dt
    
    vx_0 -= (x_0 / dist_cubed(x_0,y_0))*dt
    vy_0 -= (y_0 / dist_cubed(x_0,y_0))*dt
    
    t_0 += dt
    
    x += [x_0]
    y += [y_0]
    vx += [vx_0 + x_0*dt/2]
    vy += [vy_0 + y_0*dt/2]
    t += [t_0]

X = np.array(x)
Y = np.array(y)
Vx = np.array(vx)
Vy = np.array(vy)
T = np.array(t)

plt.figure(1)
plt.plot(X,Y)
plt.plot(0,0,'ro')
plt.xlabel('X')
plt.ylabel('Y')
orbit_label = 'Planetary Orbit: time step = ' + str(dt) + ', total time = ' + str(Ttot) + ', X_0 = ' + str(X_0) + ', V_0 = ' + str(V_0)
plt.title(label=orbit_label)
plt.legend(labels=('Orbit','Star'))
plt.show()

l = []

for i in range(len(x)):
    l += [x[i]*vy[i]-y[i]*vx[i]]

L = np.array(l)

plt.figure(2)
plt.plot(T,L)
plt.xlabel('time')
plt.ylabel('angular momentum')
plt.title(label='Angular Momentum Conservation')
plt.show()

l_error = []

for i in range(len(l)):
    l_error += [l[i] - l[0]]

L_error = np.array(l_error)

plt.figure(3)
plt.plot(T,L_error)
plt.xlabel('time')
plt.ylabel('angular momentum error')
plt.title(label='Error in Angular Momentum Conservation')
plt.show()

e = []

for i in range(len(x)):
    e += [dist_squared(vx[i],vy[i])/2 - 1/dist(x[i],y[i])]

E = np.array(e)

plt.figure(4)
plt.plot(T,E)
plt.xlabel('time')
plt.ylabel('energy')
plt.title(label='Energy Conservation')
plt.show()

e_error = []

for i in range(len(e)):
    e_error += [e[i] - e[0]]

E_error = np.array(e_error)

plt.figure(5)
plt.plot(T,E_error)
plt.xlabel('time')
plt.ylabel('energy error')
plt.title(label='Error in Energy Conservation')
plt.show()
