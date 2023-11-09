# Function is a first class object 

def double_ducker():
    print("Start the Double Ducker")
    def inner_fun():
        print("Inside the Inner function")
        return f"I am ok with me "
    return inner_fun

# print(double_ducker())

# print(double_ducker()())

def doSomething (work):
    print("Start worked")
    # print(work)
    work()
    print("work ended")


# doSomething(5)
# doSomething("Work is running")

def coding():
    print('coding in python')

# doSomething(coding)

def sleeping():
    print('sleeping and dreaming in python')

doSomething(sleeping)  