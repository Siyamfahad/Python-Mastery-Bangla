



#what is polymorphism







class Father(object):
    def home(self):
        print("I have a duplex house")
    def car(self):
        print("I have a honda suv")
    def phone(self):
        print("I have a Nokia 3310")
 

class Children(Father):
    def phone(self):
        print("i have an iphone 13")

son1 = Children()

father = Father()

def check_phone(person):
    person.phone()

check_phone(son1)