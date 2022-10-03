# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:55:23 2022

@author: domde
"""


for x in "banana":
    print(x)


a = "Hello, World!"
print(a+'2')
print(len(a+'2'))


txt = "The best things in life are free!"
print("free" in txt)
if "lifa" in txt:
    print("jest znalezione")
else:
    print('nie ma')
    
    
    
print("free" in txt)
print("free" not in txt)
print(not "free" in txt)

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[2:])
print(b[-2:])

a = "    Hello, World! "
print(a.upper())
aa = a.upper()
print(a)
print(aa)
aaa = a.lower()
print(aaa)
bb=a.strip()
print(bb)



a = "Hello, World!"
print(a.replace("H", "J"))
c=a.replace('L', 'c')
print(c)





a = "Hello, World!"
b = "iMIE Hello NAZWISKO Hello wiek"
print(a.split(","))
print(b.split("Hello"))


a = "Hello"
b = "World"
c = a + ' ' + b
print(c)

age2 = '36'
txt = "My name is John, I am " + age2
print(txt)


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))




quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
d='mój\"sxs\" tekst'
print(d)

e = "aababbababbbabababb"

#for i in range(20):
#    p[i] = e.find("b", p[i-1]+1)

p1=e.find("b",0)
p2=e.find("b",p1+1)
p3=e.find("b", p2+1)
p4=e.find("b", p3+1)

print(p1)
print(p2)
print(p3)
print(p4)


for x in range(2, 30, 3):
  print(x)