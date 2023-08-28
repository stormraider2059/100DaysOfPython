import random
print("****************** Welcome to Snak, Water, Gun Game ******************")
print("Rules of this game are simple: \n1. Snake beats Water \n2. Water beats Gun \n3. Gun beats Snake \n4. If both the players choose the same option, then the game is a tie/\n")
GameOptions=["Snake","Water","Gun"]
CompChoice=random.choice(GameOptions)
def gameStart():
    print("The bot has chosen its choice.\n")
    print("Your turn to chose your choice. Please choose from the following options: \n1. Snake \t2. Water \t3. Gun\n")
    PlayerChoice=int(input("Your choice: "))
    if PlayerChoice==1:         #player chose Snake
        if CompChoice=="Snake":
            print("Bot chose Snake too")
            print("Its a tie")
        elif CompChoice=="Water":
            print("Bot chose Water")
            print("You won")
            return 1
        else:
            print("Bot chose Gun")
            print("You lost")
            return 0          
    elif PlayerChoice==2:       #player chose Water
        if CompChoice=="Snake":
            print("Bot chose Snake")
            print("You lost")
            return 0
        elif CompChoice=="Water":
            print("Bot chose Water too")
            print("Its a tie")
        else:
            print("Bot chose Gun")
            print("You won")
            return 1
    elif PlayerChoice==3:       #player chose Gun
        if CompChoice=="Snake":
            print("Bot chose Snake")
            print("You won")
            return 1
        elif CompChoice=="Water":
            print("Bot chose Water")
            print("You lost")
            return 0
        else:
            print("Bot chose Gun too")
            print("Its a tie")
    else:
        print("Invalid choice. Please choose from the following options: \n1. Snake \t2. Water \t3. Gun\n")
        return gameStart()
    
start=gameStart()
print(start)