# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:26:31 2020

@author: eymenipek
"""
import matplotlib.pyplot as plt
import scipy.io
import numpy as np

DriveCycle = scipy.io.loadmat('ExampleDriveCycle.mat')
#print(type(DriveCycle))
#print(DriveCycle['V']['Time'])

time =DriveCycle['V']['Time']

time = np.concatenate(time)
time = np.concatenate(time)
time = np.concatenate(time)
print(time)

IESS1Actual = DriveCycle['V']['IESS1Actual']
IESS1Actual = np.concatenate(IESS1Actual)
IESS1Actual = np.concatenate(IESS1Actual)
IESS1Actual = np.concatenate(IESS1Actual)
print(type(IESS1Actual))
print(IESS1Actual)

plt.plot(time, IESS1Actual)
plt.show()