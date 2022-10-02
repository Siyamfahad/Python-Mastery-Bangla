x = 20

def fun1():
    x = 60
    

    def fun2():
        global x
        x = x + 40
        
        print(x)
    fun2()

fun1()
# print(x)
    
