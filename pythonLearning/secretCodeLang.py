import random
string=str(input("Enter the string: "))
choice=int(input("Enter your string operation: \n1. Encryption\t2. Decryption\n"))

if choice==1:
    def encryption():
        if(len(string)>=3):
            removeFirstChar=string[1:]
            firstCharout=string[0] 
            cookedString=removeFirstChar+firstCharout
            listOfRandomChars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
            randomThreeChars1=random.sample(listOfRandomChars,3)
            randomThreeChars2=random.sample(listOfRandomChars,3)
            jointRandomThreeChars1="".join(element for element in randomThreeChars1)
            jointRandomThreeChars2="".join(element for element in randomThreeChars2)
            encryptedString=jointRandomThreeChars1+cookedString+jointRandomThreeChars2
            print(encryptedString)
                
        else:
            revString=string[::-1]
            print(revString)
    encryption()
elif choice==2:
    def decryption():
        if(len(string)>=3):
            withoutRandomChars=string[3:-3]
            removeLastChar=withoutRandomChars[-1]           
            stringWithoutLastChar=withoutRandomChars[:-1]   
            decryptedString=removeLastChar+stringWithoutLastChar
            print(decryptedString)
                
        else:
            revString=string[::-1]
            print(revString)
    decryption()
else:
    print("Invalid choice! Please enter either 1 or 2.")
    exit(0)
