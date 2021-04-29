#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 03:13:38 2020

@author: tylerpruitt
"""


import numpy as np
import random

def shuffle():
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    types = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    cards = []
    for suit in suits:
        for letter in types:
            cards.append((letter, suit))
    
    deck = np.array(cards)
    deck.flags.writeable = False
    
    deck_dict = {}
    
    for i in range(len(deck)):
        deck_dict[i] = deck[i][0] + deck[i][1]
    
    random_cards = np.empty(len(deck), dtype=object)
    
    for j in range(len(random_cards)):
        while True:
            choice = random.choice(deck_dict)
            if choice not in random_cards:
                random_cards[j] = str(choice)
                break
            else:
                pass
    
    for k in range(len(random_cards)):
        if random_cards[k][1] != '0':
            print(random_cards[k][0], 'of', random_cards[k][1:])
        else:
            print(random_cards[k][0:2], 'of', random_cards[k][2:])

yes = ['y', 'yes', 'Y', 'YES']
no = ['n', 'no', 'N', 'NO']

while True:
    response = input("Shuffle the cards? Answer 'yes' to shuffle or 'no' to exit: ")
    if response in yes:
        shuffle()
    elif response in no:
        break
    else:
        print('Answer not accepted. Please try again.')