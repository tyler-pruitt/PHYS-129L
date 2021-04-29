#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 05:09:56 2020

@author: tylerpruitt
"""


import random
import matplotlib.pyplot

def pairGenerator(N):
    pairs = []
    for i in range(N):
        pairs.append([random.random(),random.random()])
    return pairs

def inCircle(data):
    Nin = 0
    Nout = 0
    inData = []
    outData = []
    for i in range(len(data)):
        if ( (data[i][0])**2 + (data[i][1])**2 )**(1/2) <= 1:
            Nin += 1
            inData.append([data[i][0],data[i][1]])
        else:
            Nout += 1
            outData.append([data[i][0],data[i][1]])
    return Nin, Nout, inData, outData

def dataconverter(data):
    Xdata = []
    Ydata = []
    for i in range(len(data)):
        Xdata.append(data[i][0])
        Ydata.append(data[i][1])
    return Xdata, Ydata

def scatterPlot(Xin,Yin,Xout,Yout):
    matplotlib.pyplot.scatter(Xin,Yin,color='red')
    matplotlib.pyplot.scatter(Xout,Yout,color='blue')
    matplotlib.pyplot.show()

while True:
    N = input('Enter N (press enter to exit): ')
    if N == '':
        break
    else:
        N = int(N)
        pointdata = pairGenerator(N)
        Nin, Nout, inPoints, outPoints = inCircle(pointdata)
        Xin, Yin = dataconverter(inPoints)
        Xout, Yout = dataconverter(outPoints)
        scatterPlot(Xin, Yin, Xout, Yout)
        prob = Nin / N
        print('For N = ' + str(N) + ':')
        print('N inside:', Nin)
        print('N outside:', Nout)
        print('Probability in circle: ', prob)
