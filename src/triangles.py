#!/usr/bin/python
# -*- coding: latin-1 -*-

import math
def Hypotenuse(a, b):
    return(math.sqrt(math.pow(a, 2) + b*b))

def AdjoiningA(c, b):
    return(math.sqrt(c*c-b*b))

def AdjoiningB(c, a):
    return(math.sqrt(c*c-a*a))

