#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 15:17:46 2023

@author: cedar
"""

import numpy as np
import matplotlib.pyplot as plt

#2.2
# a)
# Assign your answer to y_a

t= np.linspace(0.1,0.25,10)

y_a = ((6*t**3)-(3*t)-4)/(8*np.sin(5*t))


# Create a plot of y_a 

y_a = ((6*t**3)-(3*t)-4)/(8*np.sin(5*t))

t= np.linspace(0.1,0.25,10)

plt.plot(t,y_a)
# b)
# Assign your answer to y_b
m= np.linspace(1,5,10)

y_b = ((3*m-2)/4*m)-((np.pi/2)*m)


# Create a plot of y_b 

m= np.linspace(1,5,10)

y_b = ((3*m-2)/4*m)-((np.pi/2)*m)

plt.plot(m,y_b)

#%%

# 2.4
# a)

A= np.matrix([[1,2],[3,4],[5,6]])

print(A)

A2 = A[2,:].transport()

print(A2)

# b)

y= np.array(np.arange(0,7,1.5)).transpose

print(y)


# c)

a=2; b=8; c=4

print(a/b*c)
print(a/b/c)
print(a/(b*c))


#%%
#2.6
# Assign your answer to problem(a) as y_c, your answer to problem(b) as y_d
y_c = np.linspace(4,34,6)
y_d = np.linspace(-4,1,6)

#%%
#2.7
# Assign your answer to problem(a) as y_e, your answer to problem(b) as y_f

y_e = np.arange(-2,2,0.5)
y_f = np.arange(8,4,-.05)

#%%
#2.12
# Write down vector z and assign f(z) as y_g
z = np.linspace(-4,4,100)
y_g = (1/np.sqrt(2*np.pi))*np.exp(-1*(z**2/2))
#Create a plot of y_g versus z, label the x axis as 'frequency' and label the x axis as 'abscissa'

z = np.linspace(-4,4,100)
y_g = (1/np.sqrt(2*np.pi))*np.exp(-1*(z**2/2))

plt.plot(z,y_g)
plt.xlabel('abscissa')
plt.ylabel('frequency')
plt.grid()
# Plot the maximum value of y_g as a horizontal line

M= np.max(y_g)
plt.plot(np.array([-4,4]),np.array([M,M]))


#%%
# Write down matrix P

P = np.array([[0.035,0.0001,10,2.0],[0.020,0.0002,8,1.0],[0.015,0.0010,20,1.5],[0.030,0.0007,24,3.0],[0.022,0.0003,15,2.5]])

# Write down vector U as an expression of parameters from P

n= P[:,0]
S= P[:,1]
B= P[:,2]
H= P[:,3]

U =  ((np.sqrt(S))/n)*(((B*H)/(B+(2*H)))**(2/3))

