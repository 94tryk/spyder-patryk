# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:41:29 2022

@author: domde
"""

def silnia(n):
    if n==1: return 1
    return (n*silnia(n-1))    
    
def silnia2(n):
    x=1
    for i in range(1, n+1): x=x*i
    return x
    
    
    


#l=int(input('podaJ liczbe: '))
l=5
k=silnia2(l)
print("silnia z " + str(l) + " wynosi:" + str(k))

