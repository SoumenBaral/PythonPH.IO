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

# -------------------------------------------#

