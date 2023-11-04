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