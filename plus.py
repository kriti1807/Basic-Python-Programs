# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 16:06:26 2021

@author: Kriti Chawla
"""

print("CALCULATOR")
print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division")
p=int(input("Choose an option:"))
x=int(input("Enter Number 1="))
y=int(input("Enter Number 2="))

if p==1:
    print("The summation of the above the two numbers is", x+y)
elif p==2:
    print("The difference of the above two numbers is", x-y)
elif p==3:
    print("The product of the above the two numbers is", x*y)
else:
    print("The summation of the above the two numbers is", x//y)
    
x=float(input("Enter raduis of circle:"))

a=3.14*x*x

print("Area of the circle wit raduis",x,"is:",a)