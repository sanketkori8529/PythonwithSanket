import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([1, -1, 0])

youDict = {"s": 1, "w": -1, "g": 0}
choiceDict = {1: "Snake", -1: "Water", 0: "Gun"}

youstr = input("Enter your choice (s/w/g): ").lower()

if youstr not in youDict:
    print("Invalid choice!")
    exit()

you = youDict[youstr]

print("Computer chose:", choiceDict[computer])

if computer == you:
    print("It's a draw")

elif computer == -1 and you == 1:
    print("You win!")

elif computer == -1 and you == 0:
    print("You lose!")
    print("Try again")

elif computer == 1 and you == -1:
    print("You lose!")
    print("Try again")

elif computer == 1 and you == 0:
    print("You win!")

elif computer == 0 and you == 1:
    print("You lose!")
    print("Try again")

elif computer == 0 and you == -1:
    print("You win!")
