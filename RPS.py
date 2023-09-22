import random

def validate(check): 
    if check != "paper":
        if check != "rock":
            if check != "scissors":
                print("\ninvalid input, try again\n")
                result = 1
                return result

a = 1
while a == 1:
    nRounds = int(input("Enter an odd number of rounds: "))
    if nRounds % 2 == 1 and nRounds >= 1:
        break

UserScore = 0
MachineScore = 0
i = 0;

while i < nRounds:
    UserChoice = (input("rock, paper, scissors?\n-------------------\n"))
    options = ["rock","paper", "scissors"]
    MachineChoice = options[random.randint(0,2)]

    if validate(UserChoice) == 1:
        continue

    print(MachineChoice, end=" ")

    if MachineChoice == "rock" and UserChoice == "paper":
        UserScore = UserScore + 1
        print("\n\npoint to you")
        i = i + 1

    elif MachineChoice == "scissors" and UserChoice == "rock":
        UserScore = UserScore + 1
        print("\n\npoint to you")
        i = i + 1

    elif MachineChoice == "paper" and UserChoice == "scissors":
        UserScore = UserScore + 1
        print("\n\npoint to you")
        i = i + 1

    elif MachineChoice == UserChoice:
        print("\n\nsame result")

    else:
        MachineScore = MachineScore + 1
        print("\n\npoint to computer")
        i = i + 1

    print("\nSCORE IS: " + str(UserScore) + "  " + str(MachineScore))

if MachineScore > UserScore:
    print("\nYOU LOSE")
elif UserScore > MachineScore:
    print("\nYOU WIN!!")
