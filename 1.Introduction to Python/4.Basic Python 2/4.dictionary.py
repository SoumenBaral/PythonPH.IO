number = [12,32,43,54,56,76,78,90]
person = ['soumen','student',23,'Pirojpur']
# key value pair
# dictionary 
# object 
# hash table
# overlap with set 
# [key : value,key : value]
 
person2 = {'name':"Soumen",'age':23,'dist':'pirojpur','profession':'Baker'}
print(person2)
print(person2['name'])
print(person2.keys())
print(person2.values())
person2['Address'] = 'Haven'
person2['name'] = 'Shuvo'
del person2['profession']
print(person2)

# Special for loop for dictionary 
for key , value in person2.items():
    print(key, value)