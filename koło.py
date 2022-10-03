# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:38:30 2022

@author: domde
"""

from turtle import *
hideturtle()
def koło(rozmiar):
    penup()
    left(90)
    fd(400)
    right(90)
    pendown()
    for i in range(360):
        right(1)
        fd(rozmiar)
koło(7)  
  

exitonclick()