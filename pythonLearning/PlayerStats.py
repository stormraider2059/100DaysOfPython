class Player:
    playerName = "NewbiePlayer69"

    def defaultPlayerName(self):
        print("\n ********************* Player Stats *********************\n")
        print(f"The default player name is {self.playerName}, you can rename it if you want to.")

    def renamePlayer(self,newName):
        newName = input("Enter the new name of the player: ")
        print(f"The player has been renamed to {newName} from {self.playerName}.")
        playerObject.playerName=newName
        
    def confirmRename(self):
        confirm=input("Are you sure you want to rename the player? (Y/N): ")
        if confirm=="Y" or confirm=="y":
            self.renamePlayer(newName="")                   #calling the renamePlayer function/method using self parameter
            exit()
        elif confirm=="N" or confirm=="n":
            print("The player has not been renamed.")
            exit()
        else:
            print("Invalid input, please try again.")
            self.confirmRename()                            #calling the confirmRename function/method using self parameter
            
    availableWeapons={"M416":"AR","AKM":"AR","M762":"AR","M16A4":"NAt-AR","Silenced Pistol":"Pistol","Chainsaw":"Melee","Fist":"Melee"}
    listConversion=list(availableWeapons.keys())
    currentlySelectedWeapon=listConversion[0]            
    Armour=100
    Health=100
    state="Alive"
    playerMoney={"Dollar":5000}
    
playerObject=Player()       #this is an object of the class Player
playerObject.defaultPlayerName()
for weaponName,weaponType in playerObject.availableWeapons.items():
    print(f"Player has a weapon {weaponName} of type {weaponType}")
print(f"The player has currently selected weapon {playerObject.currentlySelectedWeapon}.")  
print(f"The player has {playerObject.Armour} armour and {playerObject.Health} health")   
print(f"The player is {playerObject.state}.")
print(f"The player has {playerObject.playerMoney['Dollar']} dollars currently.")
playerObject.Armour-=50
playerObject.Health-=30
print(f"The player has been injured, now he has {playerObject.Armour} armour and {playerObject.Health} health")
playerObject.defaultPlayerName()
playerObject.confirmRename()
playerObject.renamePlayer(newName="")