# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:17:43 2022

@author: ahmet
"""
def capitalize_str(a):
    newworldlist=a.split(" ")
    capstr=''
    for x in newworldlist:
        if x:
          if x[0].isnumeric():
              capstr=capstr+x+" "
          else:
            x=x.capitalize()   
            capstr=capstr+x+" "
        else:
           capstr=capstr+x +" "
    return capstr
a=input("Please enter a string ")         
print(capitalize_str(a)) 
        
