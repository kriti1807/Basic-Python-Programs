# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:49:20 2021

@author: Kriti Chawla
"""

"calculate area of triangle with three given sides"
import math
x=int(input(print("enter first side")))
y=int(input(print("enter second side")))
z=int(input(print("enter third side")))
s=(x+y+z)/2
a=math.sqrt(s*(s-x)*(s-y)*(s-z))
print("area of traiangle=",a)