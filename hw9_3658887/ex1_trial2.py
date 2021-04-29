#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:12:43 2020

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt
import random as r
import sys
from Lorentz import *

def ran_sol_angle():
###Generates a random unit vector on the sphere
    phi= 2*np.pi*r.random()
    thet= np.arccos(r.random()*2-1)
    return np.sin(thet)*np.cos(phi), np.sin(thet)*np.sin(phi),np.cos(thet)

def collision(P1_initial, P2_initial):
    """
    Parameters
    ----------
    P1_initial : List of fourvector components for particle 1 before collision.
    P2_initial : List of fourvector components for particle 2 before collision.

    Returns
    -------
    P1_final : List of fourvector components for particle 1 after collision.
    P2_final : List of fourvector components for particle 2 after collision.
    """
    phi = 2*np.pi*r.random()
    theta = np.arccos(2*r.random()-1)
    
    r1 = np.sqrt(P1_initial[1]**2 + P1_initial[2]**2 + P1_initial[3]**2)
    r2 = np.sqrt(P2_initial[1]**2 + P2_initial[2]**2 + P2_initial[3]**2)
    
    x1, y1, z1 = r1*np.sin(theta)*np.cos(phi), r1*np.sin(theta)*np.sin(phi), r1*np.cos(theta)
    norm1 = np.sqrt(x1**2 + y1**2 + z1**2)
    x1, y1, z1 = x1/norm1, y1/norm1, z1/norm1 
    
    P1_final = [P1_initial[0], x1*r1, y1*r1, z1*r1]
    P2_final = [P2_initial[0], -x1*r2, -y1*r2, -z1*r2]
    return P1_final, P2_final

try:
    input_file = open('test_data.txt', 'r')
except:
    input_file = open(sys.argv[1], 'r')

input_data = []

for line in input_file:
    #print(line)
    input_data += [line.split(',')]

E_1 = float(input_data[0][0])
px_1 = float(input_data[0][1])
py_1 = float(input_data[0][2])
pz_1 = float(input_data[0][3])
E_2 = float(input_data[1][0])
px_2 = float(input_data[1][1])
py_2 = float(input_data[1][2])
pz_2 = float(input_data[1][3])

print('E_1 =', E_1, 'px_1 =', px_1, 'py_1 =', py_1, 'pz_1 =', pz_1, '\nE_2 =', E_2, 'px_2 =', px_2, 'py_2 =', py_2, 'pz_2 =', pz_2)

p_1 = np.array([E_1, px_1, py_1, pz_1])
p_2 = np.array([E_2, px_2, py_2, pz_2])

P_1 = fourvector(p_1)
P_2 = fourvector(p_2)

P_tot = P_1 + P_2

cm_boost = CM(P_tot)

p_1_cm = np.matmul(cm_boost, p_1)
p_2_cm = np.matmul(cm_boost, p_2)

collision_data_cm = np.zeros((100,2), dtype=list)

r1 = np.sqrt(p_1_cm[1]**2 + p_1_cm[2]**2 + p_1_cm[3]**2)
r2 = np.sqrt(p_2_cm[1]**2 + p_2_cm[2]**2 + p_2_cm[3]**2)
for i in range(100):
    s = ran_sol_angle()
    collision_data_cm[i] = [[p_1_cm[0], s[0]*r1, s[1]*r1, s[2]*r1], [p_2_cm[0], -s[0]*r2, -s[1]*r2, -s[2]*r2]]


cm_boost_inv = inv(cm_boost)

collision_data_lab = np.copy(collision_data_cm)
E_1_data, E_2_data = [], []
px_1_data, py_1_data, pz_1_data = [], [], []
px_2_data, py_2_data, pz_2_data = [], [], []

for i in range(100):
    for j in range(2):
        collision_data_lab[i][j] = np.matmul(cm_boost_inv, collision_data_cm[i][j])
        if j == 0:
            E_1_data += [collision_data_lab[i][j][0]]
            px_1_data += [collision_data_lab[i][j][1]]
            py_1_data += [collision_data_lab[i][j][2]]
            pz_1_data += [collision_data_lab[i][j][3]]
        else:
            E_2_data += [collision_data_lab[i][j][0]] #don't need this actually
            px_2_data += [collision_data_lab[i][j][1]]
            py_2_data += [collision_data_lab[i][j][2]]
            pz_2_data += [collision_data_lab[i][j][3]]
        
fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot particle 1 points
ax.scatter(px_1_data, py_1_data, pz_1_data, s=15, marker='o')
# Plot particle 2 points
ax.scatter(px_2_data, py_2_data, pz_2_data, s=15, marker='^')

names = ('Particle 1', 'Particle 2')
plt.legend(labels=names)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

plt.figure()
plt.hist(E_1_data, bins=np.linspace(min(E_1_data), max(E_1_data), 10))
plt.title('Energy distribution for particle 1 after collision')
plt.xlabel('Energy')
plt.ylabel('Frequency')
plt.savefig('processed_collision_inputfile.pdf')
plt.show()


