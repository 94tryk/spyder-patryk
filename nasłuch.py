# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:52:47 2022

@author: domde
"""

we='acrtjyrtjgsdr accsr'


dl= we.find(" ")
dl2=len(we)-dl-1
print(dl)
print(dl2)


we1=we[:dl]
we2=we[-dl2:]

print(we1)
print(we2)

if dl>dl2:
    dm=dl2
else:
    dm=dl

wow=0
ooo=0
for i in range(dm):
    if (we1[i]==we2[i]):
        we1=we1[:i]+'0'+we1[i+1:]
        we2=we2[:i]+'1'+we2[i+1:]
        wow=wow+1
for i in range(dl):
    for j in range(dl2):
        if (we1[i]==we2[j]) and (j!=i):
            ooo=ooo+1
print(wow*10+ ooo)


