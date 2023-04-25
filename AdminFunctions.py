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
        productPrice = float(input("Enter product price: "))
        AddProduct(productName, productDescription, productPrice)
    elif service == 3:
        print("Delete Product")
    elif service == 4:
        print("Update Product")

def ManageOrders():
    print("Manage Orders:")

def ManageCustomers():
    print("Manage Customers:")