# -*- coding: utf-8 -*-
"""Python_Programming_Basic_Assingment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EDdm80uUN95GNRbuhi45o3tgg19OdTLO
"""

## 	Write a Python program to print "Hello Python"?
print("Hello")

## Write a Python program to do arithmetical operations addition and division.?
a= 4
b = 10
print(a+b)
print(a*b)
print(a/b)

## 	Write a Python program to find the area of a triangle?
a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))
s= (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print(area)

## Write a Python program to swap two variables?
x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)

## Write a Python program to generate a random number?
import random
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

