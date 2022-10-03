# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 17:53:53 2022

@author: domde
"""

from turtle import *


goto(200, 200)


speed(100000)
def małydywan():
    pencolor('black')
    fillcolor('green')
    begin_fill()
    fd(40)
    lt(90)
    fd(80)
    lt(90)
    fd(40)
    lt(90)
    fd(80)
    lt(90)
    end_fill()


    fd(40)
    lt(45)
    fillcolor('red')
    begin_fill()
    fd(28)
    rt(90)
    fd(28)
    lt(90)
    fd(56.5)
    lt(90)
    fd(28)
    rt(90)
    fd(28)
    lt(135)
    fd(80)
    lt(90)
    fd(80)
    end_fill()
    rt(90)
    fd(40)
    rt(180)
    pencolor('black')
    fd(40)
    
    lt(90)
    fd(80)
    lt(90)
    fd(40)
    lt(90)
    fd(80)
    lt(90)
    


    fd(40)
    lt(45)
    
    fd(28)
    rt(90)
    fd(28)
    lt(90)
    fd(56.5)
    lt(90)
    fd(28)
    rt(90)
    fd(28)
    lt(135)
    fd(80)
    lt(90)
    fd(80)
    
    rt(90)
    fd(40)
    rt(90)





def dywan():    
    for i in range(4):       
        for i in range(4):
            pencolor('black')
            małydywan()
            fd(200)
            rt(180)
        penup()
        lt(90)
        fd(80)
        rt(90)
        fd(80)
        pendown()
        fillcolor('green')
        begin_fill()
        for i in range(4):
            fd(40)
            lt(90)
        end_fill()
        penup()
        rt(180)
        fd(80)
        lt(90)
        fd(80)
        lt(90)
        lt(270)


dywan() 
exitonclick()