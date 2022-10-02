



#Decorators

def dec1(func):
    def wrapper():
        print("*************")
        func()
        print("*************")
    return wrapper

@dec1
def greet():
    print("Hello There.")
@dec1
def goodb():
    print("goodbye")
# greet()
goodb()