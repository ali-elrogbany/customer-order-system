fileName = "UserDatabase.txt"
from GeneralFunctions import *

def FindUser(email):
    file = open(fileName, "r")
    for i in file:
        userList = i.split("~")
        if userList[2] == email:
            file.close()
            return True
    file.close()
    return False

def AddUser(fullName, email,  dateOfBirth, password):
    file = open(fileName, "a+")
    if FindUser(email) == False:
        id = int(GetLastID(fileName)) + 1
        record = str(id) + "~" + fullName + "~" + email + "~" + dateOfBirth + "~" + password + "~" + "Customer" + "~"
        file.write(record + "\n")
        file.close()
        return True
    file.close()
    return False

def CheckLogIn(loginEmail, loginPassword):
    if FindUser(loginEmail) == True:
        file = open(fileName, "r")
        for i in file:
            userList = i.split("~")
            if userList[2] == loginEmail:
                if userList[4] == loginPassword:
                    return (True, userList[5])
    return (False,False)