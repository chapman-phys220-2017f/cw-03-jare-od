#!/usr/bin/env python3

"""Gaussian Module Unit Tests"""

import nose
import math
import gaussian

def test_g():
    """Tests g with following trials:
        - g(0) ?= 1.0/sqrt(2pi)
	- g(1) ?= 1.0/sqrt(2pi)*exp(-1/2)
    """
    # Pre-computed correct value of g(0) and g(1)
    actual = 1.0/math.sqrt(2*math.pi)
    actual2 = 1.0/math.sqrt(2*math.pi)*math.exp(-1/2)
    # Testing implementation
    trial = gaussian.g(0)
    trial2 = gaussian.g(1)
    # Debug messages like this are only printed if the test fails
    print("Testing g(0): ",actual," ?= ",trial)
    print("Testing g(1): ",actual2," ?= ",trial2)
    # an assert command is the actual test
    # for floats, be sure to use assert_almost_equal instead (here to 4 digits)
    nose.tools.assert_almost_equal(actual, trial, 4)
    nose.tools.assert_almost_equal(actual2, trial2, 4)

def test_interval():
    """Tests interval with the following trials:
	- interval(g,0,1,.5)
	- interval(g,0,1,.3)
    """
    # Pre-computed correct value of interval(g,0,1,.5) and interval(g,0,1,.3)
    actual = [gaussian.g(0), gaussian.g(.5), gaussian.g(1)]
    actual2 = [gaussian.g(0), gaussian.g(.3), gaussian.g(.6), gaussian.g(.9), gaussian.g(1.2)]
    # Testing implementation
    trial = gaussian.interval(gaussian.g,0,1,.5)
    trial2 = gaussian.interval(gaussian.g,0,1,.3)
    # Debug messages
    print("Testing interval(g,0,1,0.5): ",actual," ?= ",trial)
    print("Testing interval(g,0,1,0.3): ",actual2," ?= ",trial2)
    #assert
    for k in range(0,2):
   	 nose.tools.assert_almost_equal(actual[k], trial[k], 4)
    for j in range(0,4):
	    nose.tools.assert_almost_equal(actual2[j], trial2[j], 4)

def test_integrate():
    """Tests integrate with the following trial:
	- integrating from -1 to 2 with dx = 1
    """
    # Pre-computed correct value of the integral
    actual = (1/2)*(gaussian.g(-1)+2*gaussian.g(0)+2*gaussian.g(1)+gaussian.g(2))
    # Testing implementaion
    trial = gaussian.integrate(gaussian.interval(gaussian.g,-1,2,1),1)
    # Debug messages
    print("Testing the integral from -1 to 1 broken into 2 segments: ",actual," ?= ",trial)
    #assert
    nose.tools.assert_almost_equal(actual, trial)

def test_gauss_norm():
    """Tests normalization of Gaussian function with the following trial:
	-integral from -20 to 20 of the normalized Gaussian function
    """
    # Pre-computed correct value of integral(i,dx)
    actual = 1.00000
    # Testing implementation
    trial = gaussian.integrate(gaussian.interval(gaussian.g,-20,20,.1),.1)
    #Debug messages
    print("Testing integral of normalized Gaussian function from -20 to 20: ",actual," ?= ",trial)
    #assert
    nose.tools.assert_almost_equal(actual, trial, 4)
