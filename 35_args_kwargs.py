def list_fruit(val1,**kwargs):
    print(val1)
    for key,value in kwargs.items():
        print(key,value)


fruits ={'apple':30,'orange':20,'banana':12,'grape':'4kg','avocado':5}
list_fruit('nothing',**fruits)