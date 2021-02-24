#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:14:48 2020

@author: tylerpruitt
"""


def flighttime(vy):
    g = 9.8
    return 2*vy/g

def horizontaldistance(vx,vy):
    g = 9.8
    return 2*vx*vy/g

def maxheight(vy):
    g = 9.8
    return (1/2)*(vy**2)/g

vx = float(input("Enter vx: "))
vy = float(input("Enter vy: "))

if vy <= 0:
    print('cannonball does not go anywhere')
else:
    print('total flight time:', flighttime(vy), 's')
    print('total horizontal distance:', horizontaldistance(vx, vy), 'm')
    print('maximum height:', maxheight(vy), 'm')
    