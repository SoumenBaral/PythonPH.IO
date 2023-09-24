def sum (num1,num2,num3=0):
    result = num1+num2+num3
    return result

# total = sum(10,20)
# print(total)

def allSum (num1,num2,*numbers):
    print(numbers)
    sum = 0 
    for num in numbers:
        print(num)
        sum +=num
    return sum

totalSum = allSum(45,50,33,23,32)
print(totalSum)

def doALot(*args):
    print(args)