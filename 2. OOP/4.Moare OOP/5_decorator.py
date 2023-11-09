import math

def timer(func):
    def inner(*args,**kwargs):
        print("Inner started")
        # print(func)
        func(*args, **kwargs)
        print("Inner end")
    return inner
# timer()()

@timer
def get_factorial(n):
    print("factorial Starting")
    result= math.factorial(n)
    print(f'factorial of {n} is: {result}')
get_factorial(n=10)

# timer(get_factorial)()