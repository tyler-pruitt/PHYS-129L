#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 21:01:26 2020

@author: tylerpruitt
"""


import random
import matplotlib.pyplot as plt
import numpy as np
import math

def decay(p):
    u=random.random()
    if u< p:
       return -1
    else:
       return 0

n_tot= int (input("Input the total number of particles: "))
n_exp = float(input('Input the number of particles that should decay in one unit time: '))
n_runs= int (input("Input the total number of runs: "))

prob = n_exp / n_tot

m = []

for runs in range(n_runs):
    particles = n_tot*[1]
    
    for i in range(n_tot):
        if particles[i]==1:
            particles[i]= particles[i]+decay(prob)
    
    m += [particles.count(0)]

n = []

for i in range(int(min(m)),int(max(m))+1):
    n += [i]

p_n = []

for i in range(len(n)):
    p_n += [(n_exp**n[i] / math.factorial(n[i])) * np.e**(-n_exp)]

p_n = np.array(p_n)
plt.figure()
plt.hist(m, bins=20)
plt.plot(n, n_runs*p_n, 'r')
plt.ylabel("Frequency")
plt.xlabel("Number of decayed particles")
plt.title('Poisson distribution versus Experimental data')
plt.legend(('Theory','Experiment'))
plt.savefig('decay_experiment.png')
plt.show()
