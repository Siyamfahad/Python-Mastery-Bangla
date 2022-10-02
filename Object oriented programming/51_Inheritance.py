



# What Is inheritance?


class Father(object):
    def home(self):
        print("I have a duplex house")
    def car(self):
        print("I have a honda suv")

class mother():
    def sportscar(self):
        print("I have a bmw i8")

class Children(Father,mother):
    def phone(self):
        print("i have an iphone 13")

son1 = Children()

son1.car()


