balance = 300 # Global variable we can use it any where 
def fun():
    name = 'Soumen' #Its a local variable it can only use into the function and condition
    global balance
    balance = balance - 100
    print(balance)

fun() 
print(balance)
# print(name) local variable thats why we can not access it outside the function .
