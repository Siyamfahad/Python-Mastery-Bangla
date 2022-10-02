



#write a program that take user input of fruit name and quantity then calculate the price and show message

fruits = {'mango':250, 'banana':100, 'cherry':205,"grape":400,"strawberry":100}

user_fruit = input("Enter The Fruit Name : ")

for key,value in fruits.items():
    if user_fruit == key:
        quantity = int(input("How many KGs "))
        name =input("enter your name ")
        address = input("Enter your address ")
        price = value * quantity
        print(f" Thanks Mr.{name}, your {key}'s are on the way to {address}, the totall bill will be {price} ")