#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 05:17:33 2020

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt

def alpha_n(P, x, n):
    """
    

    Parameters
    ----------
    P : List of polynomials.
    x : Polynomial of order 1, e.g. np.poly1d([1,0]).
    n : Entry number of alpha to be calculated.

    Returns
    -------
    alpha : alpha value for position n.

    """
    norm_integ = np.poly1d.integ(P[n-1] * P[n-1])
    norm = norm_integ(1) - norm_integ(-1)
    
    overlap_integ = np.poly1d.integ(x**1 * P[n] * P[n-1])
    overlap = overlap_integ(1) - overlap_integ(-1)
    
    alpha = -1 * (overlap / norm)
    return alpha

def N_n(P, alpha, n):
    """
    

    Parameters
    ----------
    P : List of polynomials.
    alpha : List of alpha values.
    n : Entry number of N to be calculated.

    Returns
    -------
    N : N value for position n.

    """
    normalization = P[n-1](1) + alpha[n-1]*P[n-2](1)
    
    N = 1 / normalization
    return N

#Generate n+1 polynomials
n = int(input('Enter n: '))

P = (n+2)*[0]
alpha = (n+2)*[0]
N = (n+2)*[0]

x = np.poly1d([1,0])

P[0] = np.poly1d([1])
P[1] = x

for i in range(2,n+2):
    alpha[i-1] = alpha_n(P, x, i-1)
    N[i] = N_n(P, alpha, i)
    P[i] = np.poly1d(N[i]*(x*P[i-1] + alpha[i-1]*P[i-2]))

for i in range(len(P)):
    print(P[i])

#Generate plot
n_plot = 7

P_plot = n_plot*[0]
alpha_plot = n_plot*[0]
N_plot = n_plot*[0]

P_plot[0] = np.poly1d([1])
P_plot[1] = x

for j in range(2,7):
    alpha_plot[j-1] = alpha_n(P_plot, x, j-1)
    N_plot[j] = N_n(P_plot, alpha_plot, j)
    P_plot[j] = np.poly1d(N_plot[j]*(x*P_plot[j-1] + alpha_plot[j-1]*P_plot[j-2]))
    
plt.figure()
z = np.linspace(-1,1,100)
P_z = np.zeros((8,100))
for i in range(7):
    P_z[i] = P_plot[i](z)
    plt.plot(z,P_z[i])

plt.plot(z,P[-1](z))
names = ('n = 0', 'n = 1', 'n = 2', 'n = 3', 'n = 4', 'n = 5', 'n = 6', 'n = ' + str(n+1))
plt.legend(labels=names)
plt.title('Legendre polynomials')

