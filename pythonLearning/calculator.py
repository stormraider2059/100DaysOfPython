print("\n")
print("*** This is the calculator that performs \"addition\",\"subtraction\",\"multiplication\" and \"division\" operations on two numbers ***\n")
print("Enter whether you want to perform operation on which of the following\n")
print("\n1. Operation on integer number. \n2.Operation on floating number.\n")
choice=input("Enter your choice: ")
choice=int(choice)

#code for operations of integer numbers.
if choice == 1:  
      
    print("\n1.Addition\n")
    
    a=input("Enter first number: ")
    b=input("Enter second number: ")
    print("Addition of your two numbers implies result ",int(a)+int(b))

    print("\n2.Subtraction\n")
    
    a=input("Enter first number: ")
    b=input("Enter second number: ")
    print("Subtraction of your two numbers implies result ",int(a)-int(b))

    print("\n3.Multiplication\n")
    
    a=input("Enter first number: ")
    b=input("Enter second number: ")
    print("Multiplication of your two numbers =",int(a)*int(b))

    print("\n4.Division\n")
    
    a=input("Enter first number: ")
    b=input("Enter second number: ")
    print("Division of your two numbers =",int(a)/int(b))


#code for operations of floating numbers.

elif choice == 2:

    print("\n1.Addition\n")
    
    a=input("Enter first number: ")
    b=input("Enter second number: ")
    print("Addition of your two numbers implies result ",float(a)+float(b))

    print("\n2.Subtraction\n")
    
    a=input("Enter first number: ")
    b=input("Enter second number: ")
    print("Subtraction of your two numbers implies result ",float(a)-float(b))

    print("\n3.Multiplication\n")
    
    a=input("Enter first number: ")
    b=input("Enter second number: ")
    print("Multiplication of your two numbers =",float(a)*float(b))

    print("\n4.Division\n")
    
    a=input("Enter first number: ")
    b=input("Enter second number: ")
    print("Division of your two numbers =",float(a)/float(b))


#invalid choice from user (i.e other than integer or floating values or other than input opt 1 and 2)

else:
    print("Invalid choice! Sorry this calculator can only perform operations on integer and floating numbers.\n")
    exit(0)