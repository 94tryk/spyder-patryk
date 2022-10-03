# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 21:38:11 2022

@author: domde
"""

from turtle import *
hideturtle()
for i in range(6):
    fillcolor('green')
    begin_fill()
    fd(125)
    left(90)
    fd(125/10*3)
    left(135)
    fd(88)
    right(45+90)
    fd(3*125/10)
    left(90+45)
    fd(17)
    right(45)
    fd(4*125/10)
    right(120)
    end_fill()
right(30)

for i in range(6):
    fillcolor('red')
    begin_fill()
    fd(250)
    right(90)
    fd(250/10*3)
    right(135)
    fd(176)
    left(45+90)
    fd(3*250/10)
    right(90+45)
    fd(35)
    left(45)
    fd(4*250/10)
    left(120)
    end_fill()
exitonclick()
