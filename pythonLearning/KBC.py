print("************** KBC quiz game **************\n")
prize=[i*2000000 for i in range(10)]
#first question
def firstQuestion():
    q1=["Which of the following is the capital of India?\n 1. Delhi\t 2. Mumbai\n 3. Kolkata\t 4. Chennai\n"]
    print(q1[0])
    q1opt=[1,2,3,4]
    q1ans=int(input("Enter your answer: "))
    if q1ans==q1opt[0]:
        print("Correct answer! You have won Rs.",prize[1])
    elif q1ans==q1opt[1] or q1ans==q1opt[2] or q1ans==q1opt[3]:
        print("Wrong answer! The correct answer is :",q1opt[0],"Delhi")
        print("You have won Rs.",prize[0])
        exit(0)
    else:
        print("Invalid answer! Please choose from the given options only i.e from 1 to 4.\n")
        return firstQuestion()
a=firstQuestion()
print(a)

#second question
def secondQuestion():
    q2=['Which of the following is the capital of Maharashtra?\n 1. Delhi\t 2. Mumbai\n 3. Kolkata\t 4. Chennai\n']   
    print(q2[0])
    q2opt=[1,2,3,4]
    q2ans=int(input("Enter your answer: "))
    if q2ans==q2opt[1]:
        print("Correct answer! You have won Rs.",prize[2])
        
    elif q2ans==q2opt[0] or q2ans==q2opt[2] or q2ans==q2opt[3]:
        print("Wrong answer! The correct answer is :",q2opt[1],"Mumbai")
        print("You have won Rs.",prize[1])
        exit(0)
    else:
        print("Invalid answer! Please choose from the given options only i.e from 1 to 4.\n")
        return secondQuestion()
b=secondQuestion()
print(b)

#third question
def thirdQuestion():
    q3=["Which of the following is the capital of West Bengal?\n 1. Delhi\t 2. Mumbai\n 3. Kolkata\t 4. Chennai\n"]
    print(q3[0])
    q3opt=[1,2,3,4]
    q3ans=int(input("Enter your answer: "))
    if q3ans==q3opt[2]:
        print("Correct answer! You have won Rs.",prize[3])
        
    elif q3ans==q3opt[0] or q3ans==q3opt[1] or q3ans==q3opt[3]:
        print("Wrong answer! The correct answer is :",q3opt[2],"Kolkata")
        print("You have won Rs.",prize[2])
        exit(0)
    else:
        print("Invalid answer! Please choose from the given options only i.e from 1 to 4.\n")
        return thirdQuestion()
c=thirdQuestion()
print(c)

#fourth question
def fourthQuestion():
    q4=["Which of the following is the capital of Tamil Nadu?\n 1. Delhi\t 2. Mumbai\n 3. Kolkata\t 4. Chennai\n"]
    print(q4[0])
    q4opt=[1,2,3,4]
    q4ans=int(input("Enter your answer: "))
    if q4ans==q4opt[3]:
        print("Correct answer! You have won Rs.",prize[4])
        
    elif q4ans==q4opt[0] or q4ans==q4opt[1] or q4ans==q4opt[2]:
        print("Wrong answer! The correct answer is :",q4opt[3],"Chennai")
        print("You have won Rs.",prize[3])
        exit(0)
    else:
        print("Invalid answer! Please choose from the given options only i.e from 1 to 4.\n")
        return fourthQuestion()
d=fourthQuestion()
print(d)

#fifth question
def fifthQuestion():
    q5=["Which of the following is the capital of Kerala?\n 1. Delhi\t 2. Mumbai\n 3. Kolkata\t 4. Chennai\n"]
    print(q5[0])
    q5opt=[1,2,3,4]
    q5ans=int(input("Enter your answer: "))
    if q5ans==q5opt[2]:
        print("Correct answer! You have won Rs.",prize[5])
        print("Congratulations! You have won the game.")
    elif q5ans==q5opt[0] or q5ans==q5opt[1] or q5ans==q5opt[3]:
        print("Wrong answer! The correct answer is :",q5opt[2],"Kolkata")
        print("You have won Rs.",prize[4],"\n")
        print("Congratulations! You have won the game.")
        exit(0)
    else:
        print("Invalid answer! Please choose from the given options only i.e from 1 to 4.\n")
        return fifthQuestion()
e=fifthQuestion()
print(e)

