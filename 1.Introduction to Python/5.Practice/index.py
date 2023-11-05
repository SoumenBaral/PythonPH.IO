a  = 10
b = 10 
print(id(a))
print(id(b))

# there address will be same python memory management system handle it

# a = int(input()) # they always take input as String 

# one line multiple input 
# multiple line multiple input


# 1
lst = []

# for i in range(0,a):
#     x = int(input())
#     lst.append(x)

# print(lst)

# Split || join 

# split => string to list 
# join => list to string 

# lst = list(map(int,input().split()))
print(lst)

lst = [1,3,4,5,6]
lt = list(map(lambda x: x*2 , lst))
print(lt)

testCase = int(input())

range(val)-->start with 0 and end with val-1
for i in range(testCase):
    print(i)