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