# list---->> []
# set----->> {}
# tuple--->> ()
# set  is collection of unique items NO DUPLICATE
number = [12,32,43,54,56,76,78,90]
print(number)

set_number = set(number)
print(set_number)
set_number.add(100)#it don't maintain the order 
set_number.add(12)
set_number.add(12)
set_number.add(12)
set_number.add(12)
# though it's a collection of unique number that's why 12 will be add one time only 
# if we add something that already exist in the set then we can't add it again
print(set_number)

# print(set_number[2]) 'set' object is not subscriptable
# we cannot add value and watch value via its index number .

set_number.remove(12)

for item in set_number:
    print(item)
if 12 in set_number:
    print('12 Exist')
elif 90 in set_number:
    print('90 Exist')


A = {1,2,3,4,6}
B = {1,5,7,8,9}
print(A & B) #just common  A ^ B
print(A | B) # Common UnCommon all A U B