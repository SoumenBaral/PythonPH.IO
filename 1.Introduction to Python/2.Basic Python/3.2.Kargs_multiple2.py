def fullName(first,second ):
    name = f'{first} {second}'
    # print(name)

fullName(second='Baral',first='Soumen')
# We can give the value as we wish we just use second in first and first in second


def famousName (first ,last ,**additional):
    # print(additional)
    for key,val in additional.items():
        print(key,val)
famousName(last='proshad',first='vanu',title='Hujur' , micle ='jaction',cycle='Durango',additional='valoManus')
def fun (num1,num2):
    sum = num1+num2
    multiply = num1*num2
    div = num2/num1
    reminder = num1-num2
    return [sum,multiply,div,reminder]

result = fun(10,20)
print(result)
for number in result:
    print(number)