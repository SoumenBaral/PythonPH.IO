t = int(input())

while t != 0:
    a,b=input().split()
    a = int(a)
    b = int(b)

    # print(a,b)
    sum = 0
    if(a<b):
        for i in range(a+1,b):
            
            if i%2 != 0:
                sum+=i


    else:
        for i in range(b+1,a):
            if i%2 != 0:
                sum+=i
    
    print(sum)
    t-=1
