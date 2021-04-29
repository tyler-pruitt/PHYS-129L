#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:21:23 2020

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

def image_single_color(image, color, negative=False):
    """
    Parameters
    ----------
    image : array of shape m x n x 3.
    color : int; 0=red, 1=green, 2=blue.
    value : threashold value in which all values below will be set to 0.
    negative : boolean; if True returns the negative of the filtered image; default set to False.

    Returns
    -------
    filter_image : filtered image.
    """
    filter_image = image*0
    if negative == True:
        filter_image[:,:,color] = 255 - image[:,:,color]
    elif negative == False:
        filter_image[:,:,color] = image[:,:,color]
    else:
        print('Error with parameter negative: negative must be a boolean.')
        
    return filter_image
    
def image_filter_pixel(image, threshold, intensity='same'):
    """
    Filters image by entire pixel, only shows pixels in which all colors exceed of meet threshold.
    
    Parameters
    ----------
    image : array of shape m x n x 3.
    threshold : threashold value in which all values below will be set to 0.
    intensity: uniform value of filtered pixels. default set to same as the input image.

    Returns
    -------
    filter_image : filtered image.
    """
    filter_image = image*0
    print('Filtering with threshold', threshold)
    
    for i in range(len(image)):
        for j in range(len(image[0])):
            red, green, blue = False, False, False
            for k in range(3):
                if image[i][j][k] >= threshold:
                    if k == 0:
                        red = True
                    elif k == 1:
                        green = True
                    else:
                        blue = True
            if red == True and green == True and blue == True:
                if intensity == 'same':
                    filter_image[i][j] = image[i][j]
                elif type(intensity) == int and intensity >= 0 and intensity <= 255:
                    filter_image[i][j] = intensity, intensity, intensity
                else:
                    print('Error: Intensity must be an integer between 0 and 255.')
                    
    return filter_image

def cluster(image):
    """
    Parameters
    ----------
    image : TYPE
        DESCRIPTION.

    Returns
    -------
    record : TYPE
        DESCRIPTION.
    count : TYPE
        DESCRIPTION.
    """
    rows = len(image)
    columns = len(image[0])
    record = np.zeros((rows, columns, 3), dtype=int)
    count = 0
    
    for i in range(rows):
        for j in range(columns):
            if image[i][j].any():
                if not record[i][j].any() and not record[i+1][j].any() and not record[i][j+1].any() and not record[i-1][j].any() and not record[i][j-1].any() and not record[i+1][j+1].any() and not record[i-1][j-1].any() and not record[i-1][j+1].any() and not record[i+1][j-1].any():
                    record[i][j] = list(image[i][j])
                    count += 1
    
    return record, count

def cluster2(image, radius=1):
    """
    Parameters
    ----------
    image : TYPE
        DESCRIPTION.
    radius : TYPE, optional
        DESCRIPTION. The default is 1.

    Returns
    -------
    record : TYPE
        DESCRIPTION.
    count : TYPE
        DESCRIPTION.
    """
    rows = len(image)
    columns = len(image[0])
    record = np.zeros((rows, columns, 3), dtype=int)
    count = 0
    
    for i in range(rows):
        for j in range(columns):
            accept = True
            if image[i][j].any():
                for ri in range(-radius,radius+1,1):
                    for rj in range(-radius,radius+1,1):
                        if record[i+rj][j+rj].any():
                            accept = False
                
                if accept:
                    record[i][j] = list(image[i][j])
                    count += 1
    
    return record, count

try:
    img = plt.imread(sys.argv[1])
except:
    img =plt.imread('Christmas.jpg')

plt.imshow(img)
plt.show()

red_img = image_single_color(img, color=0)
plt.imshow(red_img)
plt.show()

green_img = image_single_color(img, color=1)
plt.imshow(green_img)
plt.show()

blue_img = image_single_color(img, color=2)
plt.imshow(blue_img)
plt.show()

filtered_img = image_filter_pixel(img, 230, 255)
plt.imshow(filtered_img)
plt.title('Filtered Image')
plt.show()

clustered_filtered_img, star_count = cluster(filtered_img)
plt.imshow(clustered_filtered_img)
plt.title('Clustered Image: Method 1')
plt.show()

print('star count =', star_count)

clustered_filtered_img2, star_count2 = cluster2(filtered_img)
plt.imshow(clustered_filtered_img2)
plt.title('Clustered Image: Method 2')
plt.show()

print('star count 2 =', star_count2)


