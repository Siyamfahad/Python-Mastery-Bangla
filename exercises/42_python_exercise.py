



#Take input from user and print tables for any number


num1 = int(input("Enter The Number: "))
num2 = int(input(f"How Many Times  do you want to multiply {num1}: "))

for i in range(1,(num2+1)):
    eql = num1 * i
    print(f"{num1} X {i} = {eql}")