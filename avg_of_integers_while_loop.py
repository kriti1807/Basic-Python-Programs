# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:22:43 2021

@author: Kriti Chawla
"""

"average of 10 numbers using while loop"

i=0
s=0
while (i<10):
    x=int(input(print("Enter number=")))
    s=s+x
    i=i+1
avg=int(s/10)
print("the avg is",avg)