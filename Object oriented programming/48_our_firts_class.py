











#how to create class and objects
from playsound import playsound
class Car():
    
    def __init__(self,color='blue',brand='brandless'):
        self.color = color
        self.brand = brand
        self.wheels = 4
    
    def start_engine(self):
        print("engine started")
        return 'done'
    def horn(self):
        playsound('Object oriented programming\horn.wav')
    
car_of_fahad = Car()


# print(car_of_fahad,car_of_someone)
print(car_of_fahad.brand)
# car_of_fahad.horn()