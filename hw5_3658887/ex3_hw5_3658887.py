#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 23:59:49 2020

@author: tylerpruitt
"""


import numpy as np
import random as r
import matplotlib.pyplot as plt

def eigvals_computer(matrix_size, runs):
    eigvals = []
    
    for run in range(runs):
        M = np.zeros((matrix_size,matrix_size), dtype=complex)
        
        for i in range(len(M)):
            for j in range(len(M)):
                M[i][j] = complex(r.normalvariate(0, 1), r.normalvariate(0, 1))
        
        M_dagger = np.conj(M)
        M_dagger = np.transpose(M_dagger)
        
        W = np.add(M, M_dagger)
        
        for i in range(matrix_size):
            eigvals += [np.linalg.eigvalsh(W)[i]]
        
    return eigvals

runs = 100
matrix_size1 = 30
matrix_size2 = 100

eigvals1 = eigvals_computer(matrix_size1, runs)
eigvals2 = eigvals_computer(matrix_size2, runs)

r1 = max(eigvals1)
r2 = max(eigvals2)
x1 = np.linspace(-r1,r1,1000)
x2 = np.linspace(-r2,r2,1000)

y1 = []
y2 = []

for i in range(len(x1)):
    y1 += [np.sqrt(r1**2 - x1[i]**2)]

for i in range(len(x2)):
    y2 += [np.sqrt(r2**2 - x2[i]**2)]

plt.figure()
plt.hist(eigvals2,bins=350,color='r')
plt.hist(eigvals1,bins=200,color='b')
plt.plot(x1,y1,'k')
plt.plot(x2,y2,'g')
plt.legend(('30x30 theory', '100x100 theory', '100x100','30x30'), loc='upper right')
plt.xlabel('Eigenvalues')
plt.ylabel('Occurance')
plt.title('Semicircular plot of the eigenvalues of W')