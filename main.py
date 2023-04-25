from DatabaseFunctions import *
import os
fileName = "database.txt"

#local variables
loggedIn = False

def WelcomeScreen():
    #os.system('cls')
    print("Welcome to Ali's shopping site!")
    print("Type the number corresponding service:")
    service = int(input("1-Register\n2-LogIn\n3-Exit\n"))
    if service == 1:
        Register()
    if service == 2:
        login()
    if service == 3:
        quit()

def Register():
    #os.system('cls')
    fname = input("Enter your full name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    dateOfBirth = input("Enter your date of birth (dd/mm/yyyy): ")
    if fname == "" or email == "" or password == "" or dateOfBirth == "":
        os.system('cls')
        print("Please fill all inputs!")
        Register()
    elif not FindUser(email):
        AddUser(fname, email, dateOfBirth, password)
    else:
        print("Sorry this email is already in use!")
        Register()
        
def login():
    #os.system('cls')
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if CheckLogIn(email, password):
        global loggedIn
        loggedIn = True
        UserPage()
    
def UserPage():
    #os.system('cls')
    h = input("Enter 1 to logout: ")
    if h == "1":
        WelcomeScreen()

WelcomeScreen()