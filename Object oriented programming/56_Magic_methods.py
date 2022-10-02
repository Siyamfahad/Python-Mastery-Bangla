



#Magic Methods

from playsound import playsound

class Car():

    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
        self.wheels = 4

    def set_wheels(self, wh):
        self.wheels = wh

    def start_engine(self):
        print("engine started")
        return 'done'

    def horn(self):
        playsound('Object oriented programming\horn.wav')

class SportsCar(Car):
    def __init__(self, color, brand, model,hp):
        super().__init__(color, brand, model)
        self.hp = hp
    def __add__(self,other):
        return self.hp + other.hp
    def __str__(self):
        return f"Object Of SportsCar Class, The Car is {self.color} color, the brand is {self.brand}"
    def __len__(self):
        return 7
    
car_of_farin = SportsCar('Black','lamborghini','aventador',740)
car_of_farin2 = SportsCar('Black','bmw','i8',369)

print(car_of_farin)
print(len(car_of_farin))
