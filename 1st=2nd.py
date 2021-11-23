# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:29:51 2021

@author: Kriti Chawla
"""

numbers_x=[10,20,30,40,10]
numbers_y=[75,65,35,75,30]

def numbers(numbersList):
    fnum=numbersList[0]
    lnum=numbersList[-1]
    if fnum == lnum:
        return True
    else:
        return False

print("for 1st list the answer is ", numbers(numbers_x))    
print("for 2nd list the answer is", numbers(numbers_y))   
    
    
   