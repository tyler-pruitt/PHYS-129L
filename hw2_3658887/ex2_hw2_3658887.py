#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:04:32 2020

@author: tylerpruitt
"""


a = float(input("Enter float number a: "))
b = float(input("Enter float number b: "))

if a > b:
    print('a is greater than b')

if a < b:
    print('a is less than b')

if a == b:
    print('a is equal to b')

if a >= b:
    print('a is greater than or equal to b')

if a <= b:
    print('a is less than or equal to b')

if a+b > 0:
    print('sum of a and b is positive')
elif a+b == 0:
    print('sum of a and b is zero')
else:
    print('sum of a and b is negative')