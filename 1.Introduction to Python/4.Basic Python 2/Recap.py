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

