"""Functions used in Exercise 8 of Geol 197 GDAM"""

# Import any modules needed in your functions here
import math

import numpy as np

# Define your new functions below
def gaussian_first(mean, stddev, x):
  return (1 / (stddev * np.sqrt(2 * np.pi)))* (np.exp(-((x - mean)**2) / (2 * stddev**2)))
def gaussian(mean, stddev, x_array):
  prob = np.zeros(len(x_array))
  for i in range(len(x_array)):
    x = x_array[i]
    prob[i] = (1 / (stddev * np.sqrt(2 * np.pi)))* (np.exp(-((x - mean)**2) / (2 * stddev**2)))
  return prob
    
