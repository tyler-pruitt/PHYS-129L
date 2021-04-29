#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:51:20 2020

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt

def julia(z, c, R=2):
    """
    Parameters
    ----------
    z : complex number.
    c : complex number.
    R : number. The default is 2.

    Returns
    -------
    iteration count: number of times z needs to be updated. If iteration count exceeds 25, returns 0.
    """
    iteration_count = 0
    while np.abs(z) <= R:
        z = z**2 + c
        iteration_count += 1
        if iteration_count > 25:
            return 0
    
    return iteration_count

xpos = np.linspace(-2,2,200)
ypos = np.linspace(-2,2,200)

img= np.array(len(xpos)*[len(ypos)*[[0,0,0]]],dtype=np.uint8)
img2=np.array(len(xpos)*[len(ypos)*[[0,0,0]]],dtype=np.uint8)
img3=np.array(len(xpos)*[len(ypos)*[[0,0,0]]],dtype=np.uint8)

for i in range(len(xpos)):
    for j in range(len(ypos)):
        z = xpos[i] + 1j*ypos[j]
        
        z_red = julia(z,c=0.5)
        z_green = julia(z,c=-0.7-0.3j)
        z_blue = julia(z,c=1j)
        
        img[i][j] = z_red, 0, 0
        img2[i][j] = 0, z_green, 0
        img3[i][j] = 0, 0, z_blue
        
img_new = img / 25
img2_new = img2 / 25
img3_new = img3 / 25

img4 = img_new + img2_new + img3_new

figure,axs=plt.subplots(2,2)

axs[0,0].imshow(img_new)
axs[0,0].set_title('c = 0.5')
axs[0,1].imshow(img2_new)
axs[0,1].set_title('c = -0.7-0.3j')
axs[1,0].imshow(img3_new)
axs[1,0].set_title('c = 1j')
axs[1,1].imshow(img4)
axs[1,1].set_title('Combined')

plt.tight_layout()
plt.show()

