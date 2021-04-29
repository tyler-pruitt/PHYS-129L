#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:06:08 2020

@author: tylerpruitt
"""


import random

def dice_generator():
    n = random.random()
    return int(6*n + 1)

def mini_battle(roll_attackers,roll_defenders,n_attackers,n_defenders):
    for i in range(min(min(n_defenders, 2),min(n_attackers,3))):
        if roll_attackers[i] > roll_defenders[i]:
            n_defenders -= 1
        elif roll_attackers[i] < roll_defenders[i]:
            n_attackers -= 1
        else:
            n_attackers -= 1
    return n_attackers, n_defenders

def battle(n_attackers, n_defenders):
    while n_attackers != 0 and n_defenders != 0:
        roll_attackers = []
        roll_defenders = []
        
        for i in range(min(n_attackers, 3)):
            roll_attackers += [dice_generator()]
        
        for i in range(min(n_defenders, 2)):
            roll_defenders += [dice_generator()]
        
        roll_attackers.sort(reverse=True)
        roll_defenders.sort(reverse=True)
        
        print("Attacker's roll:", roll_attackers)
        print("Defender's roll:", roll_defenders)
        
        n_attackers, n_defenders = mini_battle(roll_attackers, roll_defenders, n_attackers, n_defenders)
        
        print('New number of attackers:', n_attackers)
        print('New number of defenders:', n_defenders)
        
        if n_attackers == 0 or n_defenders == 0:
            break
        
        while True:
            try:
                response = input("Would you like to continue? Enter 'yes' or 'no': ")
                
                if response not in yes and response not in no:
                    raise
            except:
                print('Invalid input, please try again')
            else:
                break
        
        if response in no:
            break
    
    if n_defenders == 0:
        print('The attackers won!')
        print('Battle ended')
    elif n_attackers == 0:
        print('The defenders won!')
        print('Battle ended')
    else:
        print('Battle ended')

while True:
    n_attackers = int(input('Enter number of attackers: '))
    n_defenders = int(input('Enter number of defenders: '))
    
    yes = ['y', 'yes', 'Y', 'YES']
    no = ['n', 'no', 'N', 'NO']
    
    battle(n_attackers, n_defenders)
    
    while True:
            try:
                answer = input("Would you like to have another battle? Enter 'yes' or 'no': ")
                
                if answer not in yes and answer not in no:
                    raise
            except:
                print('Invalid input, please try again')
            else:
                break
        
    if answer in no:
        break
