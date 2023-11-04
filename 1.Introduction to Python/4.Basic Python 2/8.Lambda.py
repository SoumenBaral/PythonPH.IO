# lambda is for 1 line function

def doubled (num):
    return num*2

double = doubled(32)
print(double)

doubled2 = lambda num : num * 2 # same function one is single line function
sqr = lambda num: num*num
double2 = doubled2(20)
square = sqr(4)
print(double2,square)

# Multiple value 

sum = lambda x,y : x+y

add = sum(11,19)
print(add)

# Map 
number = [12,32,43,54,56,76,78,90]
# double_numbers = map(double,number)
double_nums = map(lambda x: x*2,number)
sqr_nums  = map(lambda x : x*x,number)

print(number)
print(list(double_nums))
print(list(sqr_nums))

# Filter 

actors = [
    {'name':"shabnur",'age':65},
    {'name':"shakira",'age':25},
    {'name':"shabila Noor",'age':65},
    {'name':"shabana ",'age': 70},
    {'name':"Alogir",'age':35},
    {'name':"shabnur",'age':65},
    {'name':"shakib",'age': 39},

]

junior = filter(lambda act : act['age']<40,actors)
print(list(junior))

