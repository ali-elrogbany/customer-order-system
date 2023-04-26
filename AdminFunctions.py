from ProductDatabaseFunctions import *
productDatabaseFile = 'ProductDatabase.txt'
userDatabaseFile = 'UserDatabase.txt'
orderDatabaseFile = 'OrderDatabase.txt'

def ManageProducts():
    print("Manage Products:")
    service = int(input("1-Products List\n2-Add Product\n3-Delete Product\n4-Update Product"))
    if service == 1:
        ListProducts()
    elif service == 2:
        productName = input("Enter product name: ")
        productDescription = input("Enter product description: ")
        productPrice = (input("Enter product price: "))
        AddProduct(productName, productDescription, productPrice)
        
    elif service == 3:
        ListProducts()
        lineDelete = int(input("Enter the ID of the of the product you wish to delete: "))
        productsFile = open(productDatabaseFile, "r")
        lineToDelete = ""
        for line in productsFile:
            product = line.split("~")
            if product[0] == lineDelete:
                lineToDelete = line
                break
        productsFile.close()
        DeleteProduct(lineToDelete)
          
    elif service == 4:
        print("Update Product")

def ManageOrders():
    print("Manage Orders:")

def ManageCustomers():
    print("Manage Customers:")