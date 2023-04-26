from GeneralFunctions import *
productDatabaseFile = 'ProductDatabase.txt'

def FindProduct(name):
    file = open(productDatabaseFile, "r")
    for i in file:
        productList = i.split("~")
        if productList[1] == name:
            file.close()
            return True
    file.close()
    return False

def ListProducts():
    productsFile = open(productDatabaseFile, "r")
    for productLine in productsFile:
        product = productLine.split("~")
        print(product)

def AddProduct(productName, productDescription, productPrice):
    if FindProduct(productName) == False:
        id = str(int(GetLastID(productDatabaseFile)) + 1)
        record = id + "~" + productName + "~" + productDescription + "~" + productPrice + "~"
        productDatabase = open(productDatabaseFile, "a")
        productDatabase.write(record + "\n")
        productDatabase.close()
        return True
    return False

#Not working properly
def DeleteProduct(lineToDelete):
    productsFile = open(productDatabaseFile, "w")
    idCounter = 0
    lineToWrite = ""
    for line in productsFile:
        idCounter = 1
        if line.strip("\n") != lineToDelete:
            productToPlace = line.split("~")
            if productToPlace[0] > idCounter:
                productToPlace[0] = idCounter + 1
                for i in productToPlace:
                    lineToWrite += i
            else:
                lineToWrite = line
            productsFile.write(lineToWrite)
    productsFile.close()
    print("Product Deleted!")
    