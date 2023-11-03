def fun ():
    a,b = input().split()
    a = int(a)
    b = int(b)
    sum = 0

    for i in range(1,b+1):
        if(i%2==0):
            sum +=a**i #i just forget that how to square it 
            # print(i)
        
    print(sum)

fun()