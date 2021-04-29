#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 05:08:01 2020

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt

#####################Here we define the magnetic field
def Mf(I,posQx,posQy,posx,posy):
    rx= posx - posQx
    ry=posy - posQy
    phi = np.arctan(ry / rx)
    #Take units to be mu_0 = 1
    mu_0 = 1
    
    def Mfx(I,rx,ry,phi):
        ans = np.zeros((len(rx),len(rx[0])))
        for i in range(len(rx)):
            for j in range(len(rx[i])):
                ans[i][j] = I*mu_0*(-np.sin(phi[i][j]))/(2*np.pi * (rx[i][j]**2+ry[i][j]**2+0.03)**(1/2))
                if rx[i][j] < 0:
                    ans[i][j] = -ans[i][j]
        return ans
    
    def Mfy(I,rx,ry,phi):
        ans = np.zeros((len(rx),len(rx[0])))
        for i in range(len(rx)):
            for j in range(len(rx[i])):
                ans[i][j] = I*mu_0*(np.cos(phi[i][j]))/(2*np.pi * (rx[i][j]**2+ry[i][j]**2+0.03)**(1/2))
                if rx[i][j] < 0:
                    ans[i][j] = -ans[i][j]
        return ans
    
    return Mfx(I,rx,ry,phi), Mfy(I,rx,ry,phi)

def input_current():
    while True:
     try:
      curr=float(input("input the current: "))
      xpos=float(input("input the x position: "))
      ypos=float(input("input the y position: "))
      return curr,xpos,ypos
     except:
       print("They need to be float")

Y,X= np.mgrid[-2:2:40j,-2:2:40j]

while True:
    try:
     n_wires=int(input("input the number of magnetic wires: "))
     if n_wires < 1:
        raise
     break
    except:
     print("Needs to be an integer bigger than 0")

U,V=0*X,0*X
x_wires = []
y_wires = []
current_wires = []

for coun in range(n_wires):
        print("For wire number %d, " % (coun+1))
        current,x,y=input_current()
        x_wires += [x]
        y_wires += [y]
        current_wires += [current]
        U+= Mf(current,x,y,X,Y)[0]
        V+=Mf(current, x,y,X,Y)[1]

plt.streamplot(X,Y,U,V)
plt.savefig('streamplot.png')
plt.show()

fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
ax.quiverkey(q, X=0.3, Y=1.1, U=5,
             label='Quiver key, length = 3', labelpos='E')
for i in range(n_wires):
    if current_wires[i] > 0:
        color = 'ro'
    else:
        color = 'bx'
    ax.plot(x_wires[i], y_wires[i], color)
plt.savefig('quiverplot.png')
print('Positive current is represented by a red . and negative current is represented by a blue X.')

