def fullName (first,last):
    name = f'Fullname is {first} {last}'
    return name
# Take parameter in order (first parameter is first and second is second)
# name = fullName('kodu','Azad')
name = fullName(last='Azad',first='kodu')
# print(name)

def famousName (first, last,**additional):
    name = f'{first} {last}'
    # print(additional['title'])
    for key,val in additional.items():
        print(key, val)
    return name 

Fname = famousName(last='proshad',first='vanu',title='Hujur' , micle ='jaction',cycle='Durango',additional='valoManus')
print(Fname)

# def function(num1,num2,args,kargs)
# return multiple things in an array
def fun (num1,num2):
    sum = num1+num2
    multiply = num1*num2
    div = num2/num1
    reminder = num1-num2
    return [sum,multiply,div,reminder]

result = fun(10,20)
print(result)