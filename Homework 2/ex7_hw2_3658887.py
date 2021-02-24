#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:59:36 2020

@author: tylerpruitt
"""


x = int(input('Enter an integer: '))

count = 0
primes = []
for num in range(2,x+1):
    isprime = True
    for i in range(2,num):
        if num % i == 0:
            isprime = False
        
    if isprime == True and num not in primes:
        count += 1
        primes.append(num)

print('number of prime numbers:', count)
ans = input("Do you want to see the list of prime numbers? Answer 'y' or 'yes' or 'Y' or 'YES' for yes: ")

if ans == 'y' or ans == 'yes' or ans == 'Y' or ans == 'YES':
    print(primes)