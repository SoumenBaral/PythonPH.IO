#Explore String 

names = 'Soumen\'s laptop' # we can escape the quit
print(names)
# MUltiline String 
name = """Salmon Khan 
    Number nai brother in low.
    that a cute slang"""
print(name)

# F sting that's look like carate in js
name2 = f'I know the man he is {name}' 
print (name2)
name3 = 'Shakib'

print(name3[3]) # print just 3 number index
print(name[2:11]) # print 2 to 11 number index
print(name[-3]) # print last 3 number index start with -1
print(name3[::-1]) #Print reverse
# String is immutable thinks thats means we can't change it

if "laptop" in names:
    print("Exist")
else:
    print("No")

print(name.upper())
print(name2.title())

# ===============================================================>

# xxxxxxx...... Tuple.....xxxxxxx

# we use 3rd bracket for list but incase of tuple we use 1st bracket
# we can return multiple things form the function

def multiple():
    return 3,5
print(multiple())
things = 'pen','fan','laptop','table' #accidental tuple when we forget to withdraw coma;
print(things) # Accidental tuple 
print(type(things)) 
print(things[-3])
print(things[::-1])
print(things[1:3])
print()

if 'fan' and 'pen' in things:
    print("Exist")
else:
    print("Not found")

# things[0] ='wagon' it's not possible immutable

nums = ([2,3,4],[34,33,12,35],[34,212,443,2212],"Soumen","Baral",'shuvo')

for pr in nums:
    # print(pr) 
    for val in pr:
        print(val) #Single value print 

# Final thing it that we use tuple for returning the multiple value from the function 

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ---------------------------------------------------------------------

# ^^^^^^^^^^^^^^^^^^^^^ Set ........................

# list---->> []
# set----->> {}
# tuple--->> ()
# set  is collection of unique items NO DUPLICATE  

number = [12,32,43,54,56,76,78,90]
print(number)

set_number = set(number)
print(set_number) # {32, 43, 12, 76, 78, 54, 56, 90}

set_number.add(100) # It don't flow the order 
set_number.add(12)
set_number.add(12)
set_number.add(12)
set_number.add(12) # It will take one 12 only 
print(set_number)

set_number.remove(12)

print(set_number)

for item in set_number:
    print(item)
if 12 in set_number:
    print('12 Exist')
elif 90 in set_number:
    print('90 Exist')
A = {1,2,3,4,6}
B = {1,5,7,8,9}
print(A & B) # just common a^b
print(A | B ) # common uncommon all

# Dictionary ----------------?

person = ['soumen','student',23,'Pirojpur']
# key value pair
# dictionary 
# object 
# hash table
# overlap with set 
# [key : value,key : value]
person2 = {'name':"Soumen",'age':23,'dist':'pirojpur','profession':'Baker'}
print(person2['name'])
print(person2)
print(person2.keys())
print(person2.values())
for key ,val in person2.items():
    print(key,val)

# Index and value in an array 

number = [12,32,43,54,56,76,78,90]

for i ,val in enumerate(number):
    print(f'index-->{i} : {val}')


# Built in Modules in python:

from math import *
from random import *
from time import sleep

lists = [1,2,3,4,5,6]

print(ceil(3.1)) # 4
print(sqrt(16))
print(factorial(4))
print(random()) # It can be any number 
print(randint(1,100)) # random integer into 1 to 100
# sleep(3)
print(choice(lists)) # it will print a random element form the lists that i have 


# Pyautogui External package 

import pyautogui

from time import sleep

# sleep(3)
# for i in range(0,1):
#     pyautogui.write("I love all programming language mostly javascript",interval=0.25)
#     pyautogui.press('enter')


# Camera

# import cv2
# cam = cv2.VideoCapture(0)
# while True:
#     _,frame = cam.read()
#     cv2.imshow('my cam',frame)
#     cv2.waitKey(1)

# ------------------------???????????=0-----------------
# # Exception in python

try:
    result = 23/0
except:
    print("Error Happened")
finally:
    ("it will be always with it ")


# lambda is for 1 line function

def doubled (num):
    return num*2

double = doubled(32)
print(double)

doubled2 = lambda num : num * 2 # same function one is single line function
sqr = lambda num: num*num
double2 = doubled2(20)
square = sqr(4)
print(double2,square)

# Multiple value 

sum = lambda x,y : x+y

add = sum(11,19)
print(add)

# Map 
number = [12,32,43,54,56,76,78,90]
# double_numbers = map(double,number)
double_nums = map(lambda x: x*2,number)
sqr_nums  = map(lambda x : x*x,number)

print(number)
print(list(double_nums))
print(list(sqr_nums))

# Filter 

actors = [
    {'name':"shabnur",'age':65},
    {'name':"shakira",'age':25},
    {'name':"shabila Noor",'age':65},
    {'name':"shabana ",'age': 70},
    {'name':"Alogir",'age':35},
    {'name':"shabnur",'age':65},
    {'name':"shakib",'age': 39},

]

junior = filter(lambda act : act['age']<40,actors)
print(list(junior))

