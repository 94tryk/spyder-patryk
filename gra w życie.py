# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:30:58 2022

@author: domde
"""
from turtle import *
import numpy as np

tb = np.array([[0, 0], [0, 0]])

def CzyZyje(j, i):
    if tb[j, i]==1:
        return True
    else:
        return False


def kropka(b, a):
    penup()
    goto(b*2, -a*2)
    pendown()
    dot(3, 'red')

def rysuj():
    for a in range(128):
        for b in range(128):
            if tb[b, a]==1:
                kropka(b, a)

def ile_zywych_sasiadow(b,a):
    ile=0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if b==0 and i==-1: continue
            if a==0 and j==-1: continue
            if b==max and i==1: continue
            if a==max and j==1: continue
            if tb[b+i-1, a+j-1]==1: 
                ile=ile+1
    return(ile)
                
def nowy_stan(b,a):
    ile = ile_zywych_sasiadow(b,a)
    ns=tb[b, a]
    if tb[b, a]==1 and (ile<2 or ile>3):
        ns=0
    elif tb[b,a]==0 and ile==3:
        ns=1
    return ns
      

def wylicz_nowy_stan():
    for a in range(max):
        for b in range(max):
            tb2[b, a]=nowy_stan(b, a)

#--początek---------------------------------------


for i in range(12):
    tb=np.concatenate((tb, tb))
max=128
tb=tb.reshape(max, max)
tb2=tb.copy()


# szybowiec
tb[1, 0]=1
tb[1, 1]=1
tb[0, 1]=1
tb[61, 60]=1
tb[62, 61]=1

# swiatla uliczne
tb[60, 60]=1
tb[61, 60]=1
tb[62, 60]=1
#-----------------------------------------

i=0
j=0
aa=tb[j,i]
tb[j,i]=5

for q in range(30):
    for i in range(max-1):
        for j in range(max-1):
            if CzyZyje(j, i):
                kropka(j, i)


#    rysuj()
    wylicz_nowy_stan()
    tb=tb2.copy
    clearscreen()
    
# 1. narysować stan aktualny
# 2. wyliczyć stan nowy
# 3. zapisać stan nowy do tablicy 'stan aktualny'
# 4. idź do p 1.

exitonclick()
                

#----------------------------------------------------
            


         
