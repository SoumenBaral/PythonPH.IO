# we use def for function thats means define the function 
# Start day 2
def add (x,y):
    addition = x+y
    return addition

addition = add(10,20)
# print(addition)

def doubleIt(x):
    return x*2

double = doubleIt(20)
print(double)

# function with default args

def sum(a,b,c):
    return a+b+c

sum1 = sum(1,2,59)
print(sum1)

def allSum(a,b,*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum +=num
    return sum

totalSum = allSum(45,50,33,23,32)
print(totalSum)

def doALot(*args):
    for arg in args:
        print(arg)
doALot(32,43,42,34,31,21,22,11) 

doALot(65,98,98,88)

# -------------------------------------------#

# KArgs multiple

def allName(first,second):
    name = f'{first} {second}'
    return name 

name = allName(second='Azad',first='kodu')
# we can change it via second and first 
print(name)
# allName('Soumen','Baral')

def famousName(first ,last ,**additional):
    name = f'{first} {last}'
    print(name)
    # return name
    # print(additional['micle'])
    for key,val in additional.items():
        print(key,val)
    return name 
Fname = famousName(last='proshad',first='vanu',title='Hujur' , micle ='jaction',cycle='Durango',additional='valoManus')
print(Fname)
def fun (num1,num2):
    sum = num1+num2
    multiply = num1*num2
    div = num2/num1
    reminder = num1-num2
    return[sum,multiply,div,reminder]

result = fun(10,20)
for i,x in enumerate(result):
    print(f'{i}---->{x}')

# Scopes  

Balance = 200 # Global variable 

def fun ():
    XName ='Soumen Baral '# its a local variable 
    global Balance # now we can modify global variable by the using of global keyword 
    Balance = Balance-100
    print(Balance)

fun()
# print(XName)

# Module


from Function import doubleIt as it

it(2)

# Built in function 

highest = max(12,23,43,53,33,11,23,4,54,23,343)
highestArray = max([12,23,43,53,33,11,23,4,54,23])
smallest = min([12,23,43,53,33,11,23,4,54,23,343])
length = len([12,23,43,53,33,11,23,4,54,23,343])


print(f'highest = {highest} highestArray = {highestArray} smallest = {smallest} length = {length}')
