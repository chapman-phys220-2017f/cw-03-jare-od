#!/usr/bin/env python3

"""Insert doc string here

"""

# Name: Jarod Penniman and Jared Love
# Student ID: 2258875 and 1818306
# Email: penni112@mail.chapman.edu and love115@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CW 03

import scipy

def g(x):
	"""Calculates a value for the normalized Gaussian function for a value x"""
	c = 1/(scipy.sqrt(2*scipy.pi))
	gaus = c*scipy.exp(-(x**2)/2)
	return gaus

def interval(f, a, b, dx):
	"""Doc String"""
	length = b-a
	num_list = []
	n = int(length/dx)
	comp_list = [f(a+i*dx) for i in range (0,n+1)]
	return comp_list

if __name__ == "__main__":
	print(interval(g,-2,2,.25))
