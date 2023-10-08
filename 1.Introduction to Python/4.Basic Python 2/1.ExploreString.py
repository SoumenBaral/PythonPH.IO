name = 'Soumen\'s Laptop' #Escape we have to use \ 
name2 = "Shuvo"
# Multiline String 
name3 = """
    Shakib Khan
    Number one
"""
name4 = f'ami {name} my clan name is {name2} {name3}'
print(name4)
#String is a sequence of character 
for char in name3:
    print(char)

print(name2[2])
print(name3[2:11])
print(name[-3])
print(name[::-1])
# Mutable means we can change it 
# immutable means we can not change it 
# name2[0]='R' # TypeError: 'str' object does not support item assignment
# we can't change the string 

if 'Laptop' in name:
    print("Exist")
else :
    print('Noo')
print(name.upper())
print(name2.lower())
print(name3.title())