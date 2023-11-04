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