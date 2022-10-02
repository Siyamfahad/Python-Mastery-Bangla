



#Take user age as input after that tell them if they can get permission to drive car or not , condition is user age should be 18--90 years to get permission,



user_age = int(input("Enter Your Age \n"))

if user_age>=18 and user_age<=90:
    print("you can drive car")
elif user_age<18:
    print("you cannot drive, you should ride cycle")
else:
    print("you cannot drive uncle, you should take rest")

