#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:40:03 2020

@author: tylerpruitt
"""


def sum5thpowers(num):
    sum = 0
    for integer in range(num,0,-1):
        sum += integer**5
    return sum

x = int(input("Enter a positive integer: "))

if x > 0:
    print(sum5thpowers(x))
else:
    print(x, 'is not a positive integer')