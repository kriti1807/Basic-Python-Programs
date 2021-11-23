# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:00:32 2021

@author: Kriti Chawla
"""

"to find to avegrage of the entered integers"

x=int(input(print("Enter total value to input")))
sum=0
y=0
for y in range(x):
    z=int(input(print("Enter integer:")))
    sum=sum+z
avg=sum/x
print("Avegrage is:",avg)