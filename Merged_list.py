# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 14:24:13 2021

@author: Kriti Chawla
"""
list1=[10,20,25,30,35]
list2 = [40,45,60,75,90]

print("list1=[10,20,25,30,35]")
print("list2 = [40,45,60,75,90]")
result_list=[]

def rlist(list1,list2):
    for i in list1:
        if i%2!=0:
            result_list.append(i)
    
    for i in list2:
        if i%2==0:
            result_list.append(i)
            
    return result_list

print("mergerd list would be=", rlist(list1,list2))
            
            