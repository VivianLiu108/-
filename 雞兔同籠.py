# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:24:15 2021

@author: user
"""

head=int(input("heads?"))
feat=int(input("feats?"))
chicken=int((4*head-feat)/2)
rabbit=int((feat-2*head)/2)
print("There are ",chicken,end="")
if chicken>1:
    print(" chickens and ",rabbit,end="")
else:
    print(" chicken and ",rabbit,end="")
if rabbit>1:
    print(" rabbits.")
else:
    print(" rabbit.")