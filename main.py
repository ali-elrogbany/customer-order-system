from UserDatabaseFunctions import *
from GeneralFunctions import *
from AdminFunctions import *
import os

#local variables
loggedIn = False

def WelcomeScreen():
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
        os.system('cls')
        print("Sorry this email is already in use!")
        Register()
        
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    access = CheckLogIn(email, password)
    if access[0] == True:
        global loggedIn
        loggedIn = True
        if access[1] == "Admin":
            AdminPage()
        elif access[1] == "Customer":
            CustomerPage()
    else:
        print("email or password incorrect") 
    
def CustomerPage():
    #Add UserPage
    pageName = "UserPage"

def AdminPage():
    print("Admin Page:")
    service = int(input("1-Manage Products\n2-Manage Orders\nManage Customers"))
    if service == 1:
        ManageProducts()
    if service == 2:
        ManageOrders()
    if service == 3:
        ManageCustomers()
    

WelcomeScreen()