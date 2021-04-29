#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:29:38 2020

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt

x_data = []
y_data = []

datafile = open('data1.txt','r')

for line in datafile:
    pos = line.find(',')
    x_data += [float(line[:pos])]
    y_data += [float(line[pos+1:-1])]

datafile.close()

x_data = np.array(x_data)
y_data = np.array(y_data)

A_range = np.linspace(0,10,50)
k_range = np.linspace(1,2,50)

S_data = np.zeros((50,50))

for j in range(len(A_range)):
    for z in range(len(k_range)):
        for i in range(len(x_data)):
            S_data[j][z] += abs(y_data[i] - A_range[j]*np.sin(k_range[z]*x_data[i]) / x_data[i])**2

index = np.where(S_data == S_data.min())
A = A_range[int(index[0])]
k = k_range[int(index[1])]

print('A =', A, '\nk =', k)

plt.figure(1)
plt.contourf(A_range, k_range, S_data)
plt.plot(A, k, 'ro')
plt.colorbar()
plt.xlabel('A')
plt.ylabel('k')
plt.title('S(A,k) plotted for different values of A,k')
plt.show()

#estimate sigma
sigma = np.sqrt( S_data.min() / len(x_data))
print('\u03C3 =', sigma)

yx = []
for i in range(len(x_data)):
    yx += [A*np.sin(k*x_data[i]) / x_data[i]]

yx = np.array(yx)

yerr = sigma

plt.figure(2)
plt.plot(x_data, y_data, 'ro', zorder=2)
plt.plot(x_data, yx, 'b-', zorder=3)
plt.errorbar(x_data, y_data, yerr, zorder=1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of data and fit with errorbars equal to \u03C3 in the data')
labels = ('data', 'fit', 'errorbars')
plt.legend(labels, loc='upper right')
plt.show()

x_bin = []
for i in range(100):
    ans = np.sum(x_data[i*100:(i+1)*100]/100)
    x_bin.append(ans)

y_bin = []
for i in range(100):
    res = np.sum(y_data[i*100:(i+1)*100]/100)
    y_bin.append(res)

plt.figure(3)
plt.plot(x_bin, y_bin, 'ro', zorder=2)
plt.plot(x_data, yx, 'b-', zorder=3)
plt.errorbar(x_bin, y_bin, np.std(y_bin), zorder=1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of averaged bined data and fit')
labels = ('averaged data', 'fit', 'errorbars')
plt.legend(labels, loc='upper right')
plt.show()

print('Yes. The fit visually improves when the averaged data is used.')