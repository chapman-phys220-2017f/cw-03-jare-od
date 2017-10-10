#!/usr/bin/env python3

"""This module has three seperate functions. g(x) takes a numerical input and
calculates the value of the Gaussian normalized function at that point.  Interval
splits a range between a and b into equal portions of length dx.  Then, it calculates
the value of an arbitary function at those points.  Integral takes a list as an input
parameter, a list such as the one that the function interval will produce.  Integral
will approximate the integral of the arbitrary function using the trapezoidal rule.
"""

# Name: Jarod Penniman and Jared Love
# Student ID: 2258875 and 1818306
# Email: penni112@mail.chapman.edu and love115@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CW 03

import scipy         ### Note, your tests fail because the scipy module was not found
                     ### For this assignment, it was better to use math
	             ### For future assignments, it's better to use numpy explicitly, which replaces math

def g(x):
	"""Calculates a value for the normalized Gaussian function for a value x"""
	c = 1/(scipy.sqrt(2*scipy.pi))
	gaus = c*scipy.exp(-(x**2)/2)
	return gaus

def interval(f, a, b, dx):
	"""Takes an arbitrary function and splits it into intervals of length dx between
	the bounds a and b.  If dx does not split the interval evenly, the ceiling will be
	taken to obtain an integer number of intervals."""
	length = b-a
	num_list = []
	n = int(scipy.ceil(length/dx))
	comp_list = [f(a+i*dx) for i in range (0,n+1)]
	return comp_list

def integrate(i, dx):
	"""Takes a list of values, i.  i is split into n equal intervals of length dx, and contains the
	values of an arbitrary function at these points. With this data, this function will approximate
	the integral of the function using the trapezoidal rule."""
	n = len(i)
	sum = i[0]+i[n-1]
	for k in range(1,n-1):
		sum += 2*i[k]
	sum = (dx/2)*sum
	return sum
