


#Four pillers of oop

# Abstraction.
# Encapsulation.
# Inheritance.
# Polymorphism.



class Car():

    a = 400

    user_paid = 2000

    membership = False

    if user_paid > 200:
        membership = True
    def __init__(self,color='transparent',brand='brandless'):
        if (self.membership):

            self.color = color
            self.brand = brand
            self.wheels = 4
    def set_wheels(self,wh):
        self.wheels = wh

    
    def start_engine(self):
        print("engine started")
        return 'done'
    
