fileName = "database.txt"
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
        id = int(GetLastID()) + 1
        record = str(id) + "~" + fullName + "~" + email + "~" + dateOfBirth + "~" + password + "~"
        file.write(record + "\n")
        file.close()
        return True
    file.close()
    return False

def GetLastID():
    file = open(fileName, "r")
    lastID = "0"
    for i in file:
        userList = i.split("~")
        lastID = userList[0]
    file.close()
    return lastID

def CheckLogIn(loginEmail, loginPassword):
    if FindUser(loginEmail) == True:
        file = open(fileName, "r")
        for i in file:
            userList = i.split("~")
            if userList[2] == loginEmail:
                if userList[4] == loginPassword:
                    return True
    return False