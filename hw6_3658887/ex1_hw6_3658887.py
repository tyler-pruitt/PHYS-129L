#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:25:05 2020

@author: tylerpruitt
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.stats import linregress


################ This defines the differential equation data ( need to look at manual for odeint in scipy

def diffeq(y,t):
     x = y[0]
     vel= y[1]
     out= [vel, -x**5]
     return out

A_0 = float(input("Input the initial position: "))
v_0 = 0

################# Smallest time to be shown
deltat= 0.01
################# Total time
Ttot=400

############### List of times to get in the solution to the differential equations
t=np.linspace(0,Ttot, int(Ttot/deltat))

amp_data = np.linspace(0, A_0, 100)

freq_data = []

for amp in amp_data:
    ###########initial data
    ini = [amp, v_0]
    
    ########### Solve the ode. The implementation of oedint is a Runge-Kutta
    solution = odeint(diffeq, ini, t )
    
    ###############  Get the position data
    x_data = np.array(solution[:,0])
    
    #################  Do the (discrete) Fourier transform
    fourier = np.fft.fft(x_data)
    
    ################  This is usually called the power spectrum. (In many applications it is binned)
    Power = abs(fourier**2)
    
    freq = np.argmax(Power[0:int(Ttot/(2*deltat))])
    
    
    ####################   Conversion to true values (total time versus discrete time bins)
    frq_true = freq/Ttot
    
    freq_data += [frq_true]

print("The correct frequency is", frq_true, "+-", 1/(2*Ttot))
print("The period is", 1/frq_true)

slope, intercept, r_value, p_value, std_err = linregress(np.log(amp_data[5:]), np.log(freq_data[5:]))

print("Slope:", slope, "\nIntercept:", intercept, "\nR value:", r_value, "\nP value:", p_value, "\nStandard Deviation Error:", std_err)

plt.loglog(amp_data, freq_data)
plt.title('Amplitude ')
plt.xlabel('Amplitude')
plt.ylabel('Frequency')
plt.show()

######################  Showing the solution (near beginning)
plt.xlim(0, 5)
plt.ylim(-2*A_0, 2*A_0)
plt.xlabel('t')
plt.ylabel('x')
plt.title('Solution to ODE')

plt.plot(t, x_data)

plt.show()

amp_arry = np.array(amp_data)
freq_arry = np.array(freq_data)

fit = np.polyfit(np.log(amp_arry[5:]), np.log(freq_arry[5:]), 1)

print(fit)

print('Frequency scales as a power of the amplitude \n Amp = Freq**k \n Scaling: k =', slope)