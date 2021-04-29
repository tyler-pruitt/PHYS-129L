#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 03:15:00 2020

@author: tylerpruitt
"""


import numpy as np

def exponential(k):
    #e^z = 1 + z + (1/2!)z^2 + (1/3!)z^3 + ...
    z = 1
    sum = 1
    for i in range(1,k):
        sum += (z**i) / np.math.factorial(i)
    return sum

print('For k = 1: ')
print('e =', exponential(1))
print('(numpy e) - (calculated e) =', np.e - exponential(1))
print('')
print('For k = 20: ')
print('e =', exponential(20))
print('(numpy e) - (calculated e) =', np.e - exponential(20))