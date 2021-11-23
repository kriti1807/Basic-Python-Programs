# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:21:18 2021

@author: Kriti Chawla
"""

i=9
prevnum=0
for i in range(1,10):
   
    x=int(input(print("Enter current number=")))
    s=x+prevnum
    print("Sum of current number", x, "and previous number",prevnum, "is=\n",s)
    prevnum=x