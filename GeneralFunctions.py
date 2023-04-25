def GetLastID(fileName):
    file = open(fileName, "r")
    lastID = "0"
    for i in file:
        userList = i.split("~")
        lastID = userList[0]
    file.close()
    return lastID
