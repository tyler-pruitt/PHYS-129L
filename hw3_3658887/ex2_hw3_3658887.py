#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 03:31:12 2020

@author: tylerpruitt
"""


import numpy as np
import scipy.special

def besselfunction(n,z,terms):
    Jsum = 0
    for i in range(terms):
        if n >= 0:
            Jsum += ( (-1)**i * (z/2)**(2*i+n) ) / ( np.math.factorial(i) * np.math.factorial(i+n) )
        else:
            Jsum += ( (-1)**i * (z/2)**(2*i+n) ) / ( scipy.special.gamma(i+1) * scipy.special.gamma(i+1+n) )
    return Jsum

yes = ['y','Y','yes','YES']
no = ['n','N','no','NO']
flag = True

while flag == True:
    while True:
        try:
            terms = int(input('Enter how many terms in the Jn(z) power series around zero to keep: '))
            if abs(terms) != terms:
                raise
        except:
            print('Invalid input, try again')
        else:
            break
    while True:
        try:
            n = int(input('Enter integer n: '))
        except:
            print('Invalid input, try again')
        else:
            break
    while True:
        z = input('Enter z: ')
        try:
            z = float(z)
        except:
            try:
                z = complex(z)
            except:
                print('Invalid input, try again')
            else:
                break
        else:
            break
    print('J' + str(n) + '(' + str(z) + ') =', besselfunction(n,z,terms))
    print('[scipy.special J' + str(n) + '(' + str(z) + ')] - [calculated J' + str(n) + '(' + str(z) + ')] =', scipy.special.jv(n,z)-besselfunction(n, z, terms))
    response = input("Do you want other values? Enter either 'yes' or 'no': ")
    if response in no:
        break
    elif response not in yes:
        while True:
            response = input("Do you want other values? Enter either 'yes' or 'no': ")
            if response in yes:
                break
            elif response in no:
                flag = False
                break
