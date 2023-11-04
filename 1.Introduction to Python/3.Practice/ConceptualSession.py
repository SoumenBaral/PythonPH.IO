# type 
x = 3.3
print(type(x))
y = 3 + 5j
print(type(y))

a = int(3.53)#male int 
print(a)

b = float(5)
print(b)

c = complex(5,2)#make it complex number we need to take 2 number first real number and second imaginary number
print(c)
# we can not convert complex to int or float 
#  we can take 1 parameter for making complex 
d = complex(4) # output will be 4 + 0j;
print(d)

# String is immutable means we can't change the value after declaration 

xx = "Hello"
# xx[0] = 'G' it's not possible 

#  Sting is Iterable 

for char in xx:
    print(char,end='')
print()


# Some builtIn function in python 
# Capitalize || upper || lower || casefold || find || count || Replace 
 

name = "soumen"

print(name.capitalize()) # Soumen
print(name.upper()) # SOUMEN  
print(name.lower()) # soumen
print(name.casefold()) # same as lower case 


# find 

soumen = "Hello world"
src = "world"
index = soumen.find(src)
print(index)

if index !=-1:
    print(f"We just find '{src}' in the index of -- '{index}' ")

else:
    print("Not found")

# Count 
# The work of count is how many char in a siring not all single single 

course = "PhiiiitrrronPhiiiitrrron"
print(course.count('i'))
print(course.count('Phiiiitrrron'))
# Module is some build in function in python like STL in cpp
from collections import Counter
print(Counter(course)) # Counter({'i': 8, 'r': 6, 'P': 2, 'h': 2, 't': 2, 'o': 2, 'n': 2})


# List 
# It's a very flexible we can add any data type in the list or array .List is like an array.

ab = "Soumen"
print(list(ab)) 

ac = ['Python']
print(ac[0])

a =['a','b']
print(*a) #we can print the value of an array by the using of it 
# Multidimensional list 
a = [[1,2,3,4,5],[4,6,'soumen','shuvo'],'It is ok']
print(a[0][2])
for pr in a :
    print(pr)

for pr in a :
   for val in pr:
       print(val)


# =======================================================
# Stl

# append || clear || copy || count || insert || pop() || remove () || Sort() || reverse()

# clear and append
a = []
a.append(3)
a.append('ok')
print(a)
print('Before clear',a)
print(a.clear())
print("After clear",a)

# Copy

a = ['x','y']
b = a.copy()
print(b) # ['x','y']

# Insert 

x = [1,3,2,4,5,6]
x.insert(2,10) # insert (first is position and second is the value you want to insert )
print(x)

# Pop is very interesting in python and remove is same 

my_list = [1,2,3,4,5]
my_list.pop()
print(my_list)

my_list.pop(2) #we can delete the value via index number wow
print(my_list)

deleted = my_list.pop(0)
print(deleted) # we can also save it 
my_list.remove(4) # remove is take the value of array not the index
print(my_list) 


# Sort and reverse

list = [50,40,30,2,20,33,10,1]
list.sort()
print(list)
list.reverse()
print(list[::]) # print as it is 
print(list[::-1]) # same as reverse function
print(list)

# Tuple: tuple is like a list but the difference is it is immutable 
# that's means we can not modify after it is created  list is [] bracket and tuple is ()
# append || clear || count || insert || pop() || remove () || Sort() || reverse()
# Any item of upper function are not valid for tuple just valid is copy()

x = [50,40,30,2,20,33,10,1]
print(tuple(x)) # (50, 40, 30, 2, 20, 33, 10, 1)


# ----------------------------------------------------------------------------------------------

# Set
# we use 3rd bracket for set
# it's Iterable , Mutable means changeable and uniq value  

# Crate a set

x = set() 
print(x)

x = set("PphHHHiiiiitronnnnnn") 
print(x) # {'p', 'r', 'o', 'n', 'h', 'i', 't', 'P', 'H'} uniq value and divided upper and lower case 

# we can add mixed type of value 
x = set([3,5,2,'soumen','shuvo',23])
print(x) # {2, 3, 5, 'shuvo', 'soumen', 23} just bracket change 

# Some function in Set

#  add || remove || pop || clear || copy || update 

my_set = {1,3,2,4}
my_set.add(34)
print(my_set)