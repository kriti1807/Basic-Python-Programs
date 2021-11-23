#OPERATORS
#Arithemetic Operators: +, -, *, /, %, **, //
x=20
y=10
print("Sum of x and y=", x+y)
print("Subtraction of x and y=", x-y)
print("Product of x and y=", x*y)
print("Division of x and y=(float value)", x/y)
print("Remainder by the division of x and y=", x%y)
print("Square of x and y=", x**y)
print("Division of x and y=(integer value)", x//y)

#Assignment Operators: =, +=, -=, *=, /=
# x=20 This line indicates the equal to operator. It menas the value 20 is assigned to the variable x.
x+=1#increments the value of x by 1, 20+1=21
print("New value of x=",x)
x-=3#decreases the value of x by 3, 21-3=18
print("New value of x=",x)
x*=1#multiplies the value of x by the given number, 18*1=18
print("New value of x=",x)
x/=3#divides the value of x by the given number, 18/3=6 (this returns a float value, so 6.0)
print("New value of x=",x)

#Comaprision Operators: <, >, <=, >=, ==, !=
if(x<y):#6<10 so it will print the value of y i.e., 10
    print(y)
elif(x>y):#if x>y, it would print value of x i.e., 6.0
    print(x)
elif(x<=y):#if value of x were less than or equal to y, it would print value of y
    print(y)
elif(x>=y):#if value of x were more than or equal to y, it would print value of x
    print(x)
elif(x==y):#if value of x were equal to y, it would print False
    print("False")
else:#if value of x were not equal to y, it would print True
    print("True")

#Logical Operators: and, or, not
if(x<y and x<5):
    print("This condition is false")
elif(x>y or y<10):
    print("This condition is false")
else:# this line would be printed because the abive two conditions are not true
    print("This condition is true")
