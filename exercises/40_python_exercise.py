



# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.

def func1(x,y,z):
     sum = x + y + z

     if x == y == z:
          sum = sum * 3
     return sum

print(func1(23,4,5))
print(func1(9,9,9))