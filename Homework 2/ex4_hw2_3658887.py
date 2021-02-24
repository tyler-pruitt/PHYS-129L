#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:29:57 2020

@author: tylerpruitt
"""


a = int(input("Enter a positive integer: "))

for num in range(1,a):
    if num % 5 != 0:
        print(num)