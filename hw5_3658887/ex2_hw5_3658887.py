#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:03:54 2020

@author: tylerpruitt
"""


import numpy as np
import matplotlib.pyplot as plt

data = []

datafile = open("Markovdata.txt",'r')

for line in datafile:
    for entry in line:
        data += [int(entry)]

datafile.close()

n00 = 0
n10 = 0
n01 = 0
n11 = 0

for i in range(len(data)):
    if i != len(data) - 1:
        if data[i] == 1 and data[i+1] == 1:
            n11 += 1
        elif data[i] == 1 and data[i+1] == 0:
            n01 += 1
        elif data[i] == 0 and data[i+1] == 0:
            n00 += 1
        elif data[i] == 0 and data[i+1] == 1:
            n10 += 1
    else:
        pass

p00 = n00 / (data.count(0)-1)
p01 = n01 / data.count(1)
p10 = n10 / (data.count(0)-1)
p11 = n11 / data.count(1)

print('p0(0) =', p00)
print('p0(1) =', p01)
print('p1(0) =', p10)
print('p1(1) =', p11)
print('')
print('maximum likelihood for p0(0) =', p00)
print('maximum likelihood for p0(1) =', p01)

P00 = np.linspace(p00-0.15,p00+0.15,100)
P01 = np.linspace(p01-0.15,p01+0.15,100)

L = np.zeros((100,100))

for i in range(len(P00)):
    for j in range(len(P01)):
        #L[i][j] = P00[i]**n00 + (1-P00[i])**n10 + P01[j]**n01 + (1-P01[j])**n11
        L[i][j] = n00*np.log(P00[i]) + n10*np.log(1-P00[i]) + n01*np.log(P01[j]) + n11*np.log(1-P01[j])

plt.figure()
plt.contour(list(P00),list(P01), L)
plt.plot(p00,p01, 'ro')
plt.legend(('max(p0(0), p0(1))',''))
plt.title('Markov Chain Process')
plt.xlabel('p0(0)')
plt.ylabel('p0(1)')

x = np.linspace(0,1,1000)

p00_prob = (x**((p00)))*((1-x)**(1-(p00)))
p01_prob = (x**((p01)))*((1-x)**(1-(p01)))

plt.figure()
plt.plot(x,p00_prob)
plt.plot(x,p01_prob)
plt.yscale('log')
plt.title('Maximum of p0(0) and p0(1)')
plt.xlabel('Probability of result')
plt.ylabel('Probability of p0(0) and p0(1)')
plt.legend(('p0(0) probability', 'p0(1) probability'))

outfile = open('markov_data_analysis.txt', 'w')

outfile.write('p0(0) = probability of zero staying zero = ' + str(p00) + '\n')
outfile.write('p0(1) = probability of one turning into zero = ' + str(p01) + '\n')
outfile.write('p1(0) = probability of zero turning into one = ' + str(p10) + '\n')
outfile.write('p1(1) = probability of one staying one = ' + str(p11) + '\n')
outfile.write('maximum likelihood for p0(0) = ' +str(p00) + '\n')
outfile.write('maximum likelihood for p0(1) = ' +str(p01))

outfile.close()