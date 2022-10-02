








#what is constructor
#what is attributes
#what is methods



from playsound import playsound
class Car():

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
    def horn(self):
        playsound('Object oriented programming\horn.wav')
    
car_of_fahad = Car('blue','honda')
car_of_someone = Car("white","mahindra")
truck = Car("white","mahindra")
truck.set_wheels(8)

print(truck.wheels)


# print(car_of_fahad,car_of_someone)
# print(car_of_fahad.brand)
# car_of_fahad.horn()