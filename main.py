# !Importing random so that computer can choose randomly between the options

import random

# !Initially the points for computer and user are 0

comPoints = 0
usrPoints = 0

# !The actual game code


def game():

    # !These are the choices which user or the computer will be limited to
    # *ChoiceDup is same as the Choices but with lowerCase for the sake of simplicity

    Choices = ["Stone", "Paper", "Scissor"]
    ChoiceDup = []

    for i in Choices:
        ChoiceDup.append(i.lower())

    # !Taking Input from the user and removing unwanted spaces from the input

    usrInput = input("Enter 1 for Stone , 2 for Paper and 3 for Scissor \n").replace(
        " ", ""
    )

    if usrInput.isdigit():
        usrInput = int(usrInput)
        if usrInput <= 3 and usrInput >= 1:
            usrInput = usrInput - 1
        else:
            print(f"{usrInput} is not a valid Input")
    elif usrInput.isalpha():
        usrInput = usrInput.lower()
        usrInput = ChoiceDup.index(usrInput)

    usrChoice = Choices[usrInput]
    # print(usrInput)
    # print(f"You selected {Choices[usrInput]}")

    # ! value = [value which has more impact , value which has less impact] ;

    valDict = {
        "stone": ["paper", "scissor"],
        "paper": ["scissor", "stone"],
        "scissor": ["stone", "paper"],
    }

    winTexts = [
        "HaHa, This seems easy",
        "Why am I even playing against a noob",
        "Huh , No doubts I'm gonna rule this world",
        "Atleast give me some competetion",
    ]
    losingTexts = [
        "I think I need some practice",
        "Maybe, Some other day",
        "How can somebody play this good",
        "Impossible! You must be cheating",
    ]

    def result(choices):
        global usrPoints
        global comPoints
        ComputerChoice = random.choice(choices)
        print(f"You Chose: {usrChoice}")
        print(f"Computer Chose: {ComputerChoice} \n")
        if ComputerChoice == usrChoice:
            print("It's a draw")
        elif valDict[ComputerChoice.lower()].index(usrChoice.lower()) == 0:
            print("You won")
            print(random.choice(losingTexts), "\n")
            usrPoints += 1
        else:
            print("You lost \n")
            print(random.choice(winTexts), "\n")
            comPoints += 1

        print(f"Computer Points: {comPoints}")
        print(f"User Points: {usrPoints} \n")

    result(Choices)


def gamePlay():
    for i in range(11):
        game()


gamePlay()


def winner():
    if usrPoints > comPoints:
        print("Congratulations, You won")
    elif usrPoints == comPoints:
        print("Draw")
    else:
        print("You lost")


winner()


def pointReset():
    global usrPoints
    global comPoints

    usrPoints = 0
    comPoints = 0


def playAgain():
    playAgain = input(
        "Wanna Play again? Press Y to play again or N to exit \n").lower()

    if playAgain == "y":
        gamePlay()
    elif playAgain == "n":
        print("Thank you for playing")
    else:
        print("Input not recognized")


playAgain()
