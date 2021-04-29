#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:46:54 2020

@author: tylerpruitt
"""


number = float(input("Enter a float number: "))

if int(number) == number:
    print('number is an integer')

isNeg = False
if number < 0:
    isNeg = True
    print('number is negative')

def cube(num):
    return num**3

print('cube of ' + str(number) + ' is ' + str(cube(number)))

def cuberoot(num):
    if isNeg == False:
        return num**(1/3)
    else:
        ans = abs(num)
        return -ans**(1/3)

print('cube root of ' + str(number) + ' is ' + str(cuberoot(number)))