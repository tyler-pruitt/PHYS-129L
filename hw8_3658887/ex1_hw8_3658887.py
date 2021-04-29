#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:12:29 2020

@author: tylerpruitt
"""

import numpy as np
import random as r
import matplotlib.pyplot as plt

def update(x, a):
    """
    Parameters
    ----------
    x : float.
    a : float.

    Returns
    -------
    x : either updated x or original x.

    """
    y = 2*a*r.random() - a
    p_x = (1/ np.sqrt(2*np.pi)) * np.exp(-x**2 / 2)
    p_xy = (1/ np.sqrt(2*np.pi)) * np.exp(-(x + y)**2 / 2)
    
    if p_xy >= p_x:
        x += y
    elif r.random() <= (p_xy/p_x):
        x += y
    return x

def autocorrelate(x, sigma, m):
    """
    Parameters
    ----------
    x : list of x values.
    sigma : standard deviation value.
    m : positive int value.

    Returns
    -------
    output : autocorrelation function values for each m.

    """
    summ = 0
    count = len(x) - int(m)
    
    for i in range(count):
        summ += (x[i] * x[i+int(m)]) / (sigma**2)
            
    output = summ / count
    
    return output

def gauss(x_lst):
    """
    Parameters
    ----------
    x_lst : list of x values.

    Returns
    -------
    p_x : list of gaussian function values.

    """
    p_g = len(x_lst)*[0] #same structure as x
    for i in range(len(x_lst)):
            p_g[i] = (1 / np.sqrt(2*np.pi)) * np.exp(-(x_lst[i]**2) / 2)
    
    return p_g



a = np.linspace(0.1,3,10)
x_data = [ [] for _ in range(10) ] #10 lists for 10 different a's

for _ in range(10000): #for each round
    x = r.random()- 0.5 #pick a new random x in [-0.5,0.5]
    for i in range(len(a)):
        x_new = update(x, a[i]) #try to update x
        if x_new != x:
            x_data[i] += [x_new] #if x is updated save it



mean = []
std = []
N_data = []
fail_rate = []

for i in range(len(x_data)):
    mean += [np.mean(x_data[i])]
    std += [np.std(x_data[i])]
    N_data += [len(x_data[i])]
    fail_rate += [1 - (N_data[-1] / 10000)]

for i in range(10):
    print('a:', a[i], '\n mean:', mean[i], '\n std:', std[i], '\n N_data:', N_data[i], '\n fail_rate:', fail_rate[i], '\n')




M = np.linspace(0,30,31)
auto_correlate = np.zeros((10,31))
for i in range(len(x_data)):
    for j in range(len(M)):
        auto_correlate[i][j] = autocorrelate(x_data[i], std[i], M[j])




x_gauss = np.linspace(-4,4,100)
p_gauss = gauss(x_gauss)
p_gauss = np.array(p_gauss)



#Plot autocorrelation versus m for each a
fig, ax = plt.subplots(2,5, figsize=(15,7), squeeze=False)
k = 0

for i in range(2):
    for j in range(5):
        ax[i,j].plot(M, auto_correlate[k])
        ax[i,j].set_title('a: ' + str(round(a[k],2)) + '\nfail_rate: ' + str(round(fail_rate[k], 2)))
        if i == 1:
            ax[i,j].set(xlabel='m')
        if j == 0:
            ax[i,j].set(ylabel='Autocorrelation')
        k += 1

for ax in ax.flat:
    ax.label_outer()

fig.suptitle('m vs. Autocorrelation')
fig.tight_layout()
plt.savefig('m vs. autocorrelation.png')
plt.show()



#Plot x data in a historgram with the gaussian theory overlayed for each a
fig, ax = plt.subplots(2,5, figsize=(15,7), squeeze=False)
k = 0

for i in range(2):
    for j in range(5):
        ax[i,j].hist(x_data[k], bins=np.linspace(-4,4,20))
        hist_data = np.histogram(x_data[k], bins=np.linspace(-4,4,20))
        ax[i,j].plot(x_gauss, (max(hist_data[0]) / np.max(p_gauss))*p_gauss, 'tab:orange')
        ax[i,j].set_title('a: ' + str(round(a[k],2)) + '\nsigma: ' + str(round(std[k], 2)))
        if i == 1:
            ax[i,j].set(xlabel='x')
        if j == 0:
            ax[i,j].set(ylabel='Frequency')
        k += 1

for ax in ax.flat:
    ax.label_outer()

fig.suptitle('Gaussian distribution model versus data')
fig.tight_layout()
plt.savefig('Monte Carlo gaussian distribution')
plt.show()
