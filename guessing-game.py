import random

while True:

    LOWEST_NUMBER=input("What is the lowest number you want to guess between: \n")
    LOWEST_NUMBER=int(LOWEST_NUMBER)

    HIGHEST_NUMBER=input("What is the highest number you want me to guess between: \n")
    HIGHEST_NUMBER=int(HIGHEST_NUMBER)

    randomNumber = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
    userGuess = 0

    while randomNumber != userGuess:
        userGuess=input("Guess a number between " + str(LOWEST_NUMBER) + " and " +  str(HIGHEST_NUMBER) + " : \n")
        userGuess=int(userGuess)

        print("You guessed:", userGuess)

        if randomNumber > userGuess:
            print("The number is higher!")
            LOWEST_NUMBER = userGuess

        elif randomNumber < userGuess:
            print("The number is lower!")
            HIGHEST_NUMBER = userGuess

    print("You are correct!")

    playAgain=input("Do you want to play again? \n (y/n) \n")
    
    if playAgain == "n":
        break;