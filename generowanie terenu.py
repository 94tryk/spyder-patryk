# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 00:39:13 2022

@author: domde
"""

from turtle import *
import random 
speed(10000)



fillcolor('blue')
begin_fill()

penup()
goto(-1500, 1000)
pendown()
for i in range(2):
    fd(3000)
    rt(90)
    fd(2000)
    rt(90)
end_fill()

def teren():
    speed(100000)
    penup()
    fd(16)
    left(120)
    fd(16)
    rt(120)
    pendown()
    fillcolor('green')
    begin_fill()
    for i in range(6):
        rt(60)
        fd(16)
    
    end_fill()
    penup()
    rt(60)
    fd(16)
    lt(60)
    back(16)
    pendown()

penup()
goto(-910, 530)
pendown()


kol=50
wier=50

x = [0 for x in range(kol*wier)]

for i in range(kol*wier):
    los=random.random()     
    if (x[i-1]==0):
        if (x[i-kol+1]==0):
            if (x[i-kol]==0):
                if (x[i-kol-1]==0):
                    if (los<0.94):
                        x[i]=0
                    else:
                        x[i]=1
                else:
                    if los>0.8:
                        x[i]=1
                    else:
                        x[i]=0
            else:
                if los>0.7:
                    x[i]=1
                else:
                    x[i]=0
        else:
            if los>0.5:
                x[i]=1
            else:
                x[i]=0
    else:
        if los>0.3:
            x[i]=1
        else:
            x[i]=0


#for i in range(kol*wier):
#    print(str(i) + " " + str(x[i]) + " " + str((i+1) % kol))



for i in range(kol*wier):
    if (x[i]==0):
         teren()
         penup()
         fd(20)
         pendown()
    else:
         penup()
         fd(20)
         pendown()
    if i>0 and ((i+1) % kol)==0:
         penup()
         back(kol*20)
         rt(90)
         fd(20)
         lt(90)
         pendown()
    else:
         penup()
         pendown()


def drzewo():
    fillcolor('brown')
    begin_fill()
    fd(2)
    lt(90)
    fd(7)
    lt(90)
    fd(4)
    lt(90)
    fd(7)
    lt(90)
    fd(2)
    end_fill()
    fd(2)
    lt(90)
    fd(7)
    rt(90)
    penup()
    fd(2)
    pendown()
    fillcolor('green')
    begin_fill()
    for i in range(9):
    
        for j in range(5):
            lt(20)
            fd(1)
        rt(60)
    end_fill()
def drzewa():
    drzewo()
    penup()
    back(2)
    rt(90)
    fd(9)
    lt(90)
    fd(4)
    pendown()
    drzewo()
    penup()
    back(2)
    rt(90)
    fd(8)
    lt(90)
    back(11)
    pendown()
    drzewo()
    back(2)
    penup()
    rt(90)
    fd(9)
    lt(90)
    fd(1)
    lt(90)
    fd(5)
    rt(90)
    pendown()
penup()
goto(-910, 530)
pendown()

for i in range(kol*wier):
    if x[i]==0 and x[i-1]==0 and x[i-kol]==0 and x[i+kol]==0 and x[i+1]==0:
        losy=random.random()
        #print(str(i) + " " + str(losy))
        if losy<0.4:
            if losy<0.07:
                drzewo()
                penup()
                fd(20)
                pendown()
            else:
                drzewa()
                penup()
                fd(20)
                pendown()
        else:    
            penup()
            fd(20)
            pendown()
    else:    
        penup()
        fd(20)
        pendown()
    if i>0 and ((i+1) % kol)==0:
        penup()
        back(kol*20)
        rt(90)
        fd(20)
        lt(90)
        pendown()
    else:
        penup()
        pendown()


exitonclick()