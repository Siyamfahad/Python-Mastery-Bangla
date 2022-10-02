




#build rock paper scissors game

import random

user = input("Enter a choice (rock , paper, scissors) : ")

actions = ['rock','paper','scissors']
computer = random.choice(actions)


print(f" You chose {user} and computer chose {computer} ")


if user == computer:
    print("both of you chose same, so its a tie")
elif user == 'rock':
    if computer =='scissors':
        print("rock smashes scissors, you win")
    else:
        ("paper covers rock, you lose")
elif user =="paper":
    if computer =="rock":
        print("paper covers rock, you win")
    else:
        print("scissors cuts paper, you lose")
elif user =="scissors":
    if computer == "paper":
        print("scissors cuts paper , you win")
    else:
        print("rock smashes scissors , you lose")
