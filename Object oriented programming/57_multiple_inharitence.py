




# What Is Multiple inheritance?


class Father():
    def home(self):
        print("I have a duplex house")
    def car(self):
        print("I have a honda suv")

class Mother():
    def sportscar(self):
        print("i have a BMW I8")

class Children(Father,Mother):
    def phone(self):
        print("i have an iphone 13")

son1 = Children()

son1.sportscar()


