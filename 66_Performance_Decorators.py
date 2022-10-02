


from time import time
def performance(func):
    def wrapper(*args,**kwargs):
        t1 = time()
        result = func(*args,**kwargs)
        t2 = time()
        print(f"the function took {t2-t1} seconds")
        return result
    return wrapper

# @performance
# def fun1():
#     for i in range(1000000):
#         i*3

# fun1()

@performance
def fun2():
    for i in range(90000000):
        i *9 
fun2()