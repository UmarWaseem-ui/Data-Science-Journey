import random

computer = random.choice([-1, 0, 1])
user = input("Enter your choice: ")
Dict = {"r": -1, "p": 0, "s": 1}
reverseDict = {-1: "Rock", 0: "Paper", 1: "Scissor"}

you = Dict[user]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("Its a Draw !")

else:
    if(computer == -1 and you == 1):
        print("You lose !")

    elif(computer == -1 and you == 0):
        print("You win !")

    elif(computer == 1 and you == -1):
        print("You win !")

    elif(computer == 1 and you == 0):
        print("You lose !")

    elif(computer == 0 and you == -1):
        print("You lose !")

    elif(computer == 0 and you == 1):
        print("You win !")

    else:
        print("Something went wrong !")