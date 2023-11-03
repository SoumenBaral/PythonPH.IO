f = int(input())

if f == 1:
    print(0)

else:
    fibo =[0,1]
    m = 2
    while m<f:
        fibo.append(fibo[m-1]+fibo[m-2])
        m+=1
    for num in fibo:
        print(num,end = " ") # we can separate an array by the using of end =
        