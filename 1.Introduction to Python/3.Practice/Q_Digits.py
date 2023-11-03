t = int( input())
while t!=0:
    numbers = input()
    reversedNumbers = numbers[::-1]
    result = " ".join(reversedNumbers)
    print(result)
    t=t-1

#Alternative 
# 
# # t = input()
# intT = int(t)
# while intT>0:
#     val = input()
#     reversedVal = val[::-1]
#     rev =""
#     for c in reversedVal:
#         rev += c + " "

#     # rev = rev.rstrip()
#     print(rev)
#     intT -=1

 