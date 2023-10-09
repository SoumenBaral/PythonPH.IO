def multiple():
    return 3,4

# print(multiple())

things = 'pen','fan','laptop','table' #accidental tuple when we forget to withdraw coma;
print(things) 
print(type(things))
print(things[0])
print(things[-3])#we can get the value in back by the using of minus  and it starts with -1
print(things[::-1])#we can reverser any string via it 
print(things[1:4]) #we can slice it 
print('\n')

if 'pen'and 'fan' in things:
    print(
        "Exist"
    )

for item in things:
    print(item)

# things[0]='wagon' it is immutable we can not change it or assign it after declaration 

num = ([2,3,4],[34,33,12,35],[34,212,443,2212])
# print(type(num))
print(num[0])
# num[0]=[3,45] we Can not change it but

num[0][2] =33
print(num)
# Full and final thing is that we have to use tuple for returning the multiple value 
