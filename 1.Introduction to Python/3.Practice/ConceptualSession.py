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

# append || clear || copy || count() || insert() || pop() || remove ()

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