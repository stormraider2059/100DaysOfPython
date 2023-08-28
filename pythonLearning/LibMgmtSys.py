print("\n")
print("******************** Welcome to the Library Management System ********************")
print("\n")

class LibrarySem1:
    __booksSet1=["C-Programming","Digital Logic","Introduction to Information Technology","Mathermatics-I","Physics"]
    __itemsStored1=len(__booksSet1)
    __no_of_books1=__itemsStored1
    
    def __addBooks1(self,newBooks1):
        self.__booksSet1.extend(newBooks1)
        self.__itemsStored1 = len(self.__booksSet1)
        self.__no_of_books1=self.__itemsStored1
             
    def __checker1(self):
        if self.__no_of_books1==self.__itemsStored1:
            print("Library of Semester 1 is working fine.")
        else:
            print("There is some problem with the library of Semester 1.")
            
            
class LibrarySem2:
    __booksSet2=["OOP in C++","Microprocessor","Discrete Mathematics","Statistics-I","Mathematics-II"]
    __itemsStored2=len(__booksSet2)
    __no_of_books2=__itemsStored2
    
    def __addBooks2(self,newBooks2):
        self.__booksSet2.extend(newBooks2)
        self.__itemsStored2 = len(self.__booksSet2)
        self.__no_of_books2=self.__itemsStored2
    
    def __checker2(self):
        if self.__no_of_books2==self.__itemsStored2:
            print("Library of Semester 2 is working fine.")
        else:
            print("There is some problem with the library of Semester 2.")
            
            
class LibrarySem3:
    __booksSet3=["Data Structures and Algorithms","Computer Architecture","Numerical Methods","Statistics-II","Computer Graphics"]
    __itemsStored3=len(__booksSet3)
    __no_of_books3=__itemsStored3
    
    def __addBooks3(self,newBooks3):
        self.__booksSet3.extend(newBooks3)
        self.__itemsStored3 = len(self.__booksSet3)
        self.__no_of_books3=self.__itemsStored3

    def __checker3(self):
        if self.__no_of_books3==self.__itemsStored3:
            print("Library of Semester 3 is working fine.")
        else:
            print("There is some problem with the library of Semester 3.")
            

sem1Obj=LibrarySem1()
newBooks1=[]                        #add books of Semester 1 here
sem1Obj._LibrarySem1__addBooks1(newBooks1)
print(f"Number of books in Semester 1 are: {sem1Obj._LibrarySem1__itemsStored1}")
print(f"Books in Semester 1 are: ")
for bookItems1 in sem1Obj._LibrarySem1__booksSet1:
    print(f"{bookItems1}")
sem1Obj._LibrarySem1__checker1()


sem2Obj=LibrarySem2()
newBooks2=["Graphics Designing"]            #add books of Semester 2 here
sem2Obj._LibrarySem2__addBooks2(newBooks2)
print(f"Number of books in Semester 2 are: {sem2Obj._LibrarySem2__itemsStored2}")
print(f"Books in Semester 2 are: ")
for bookItems2 in sem2Obj._LibrarySem2__booksSet2:
    print(f"{bookItems2}")
sem2Obj._LibrarySem2__checker2()



    
sem3Obj=LibrarySem3()
newBooks3=["Web Development"]                      #add books of Semester 3 here
sem3Obj._LibrarySem3__addBooks3(newBooks3)
print(f"Number of books in Semester 3 are: {sem3Obj._LibrarySem3__itemsStored3}")
print(f"Books in Semester 3 are: ")

print(f"Number of books in Semester 3 are: {sem3Obj._LibrarySem3__itemsStored3}")
for bookItems3 in sem3Obj._LibrarySem3__booksSet3:
    print(f"{bookItems3}")
sem3Obj._LibrarySem3__checker3()

def persistCheck():
    print("No my program does not persist the books as the books are stored in the form of lists and are only accessible when the program is running.\n",
    "If the program is closed, the list will be destoyed and the books will be lost.")
persistCheck()

           