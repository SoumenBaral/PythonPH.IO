print('Recap Day Start....')
# --------variable---------
age = 23
tax = 33.32
# print('total price is = ',age*tax)
isActive = True
name = ' Soumen'
Address = "Pasharibunia Bhandria pirojpur"
text = f'My name is {name} and my address is {Address}'# very use full we use it in js via caret sign ;
# print(text)

# ================Taking input==========
# print("I am a honest man")
# money = input('Give me some money : ') 
# print(int(money)+100)
# firstMoney = input('Shakib khan money : ')
# secondMoney = input('Porimoni money : ')
# print(f'shakib khane gave {firstMoney} and poriMoni gave {secondMoney}')
# total = firstMoney + secondMoney
# print('false total is == ',total)
# print(type(total))
# actualTotal = int(firstMoney) +int(secondMoney)
# print('Actual total is ', actualTotal)
# print(type(actualTotal))

# Operator 

# + , - , * , / , % , //(flor modulus) 
first = 33
second = 3
# print(first%second) # vagses
# print(first//second) # vagfol 
 
#,,,,,,,,<Comparison>,,,,,,,,,,,,,
# < , > , <= , >= , == , != 
# python don't have any ++ , -- operator 
# += , -= , *= , /=
# in , not , not in , is ,is not
# and , or

# ................Condition ...................
a = 2
if a>10:
    print('Good luck')
elif a>5:
    print('Middle luck') 

elif a==2:
    print('khape khap')

else:
    print('Bad luck')
boss = True
if (3>21 ):
    print('Thik ase')
    if (boss is not False or 22<3):
        print('Boss vala')

else:
    print('jibon ta badona ')

# --->->->->For loop <-<-<-<---

numbers = [10,20,30,40,50,34,21,22,54,65]
sum = 0
for num in numbers:
    # print(num)
    sum +=num
    # if(sum>200):
    #     print('Bigger Value')

# print(sum)
text = 'Ami to vala na vala loia thioko '
for char in text:
    print(char)

for i in range(1,10,3):
    print(i)

friends =['shakib','shuvo','rakib','durjoy']
for i, friend in enumerate(friends):
    print(f"Friend No {i}---{friend}")
for i in range(5):
    print(i)

# ==<> while loop 
print('while loop ')
num = 1
while num<=10:
    num +=1
    if num == 5:
        continue
    print(num)


# Day 1 done...





