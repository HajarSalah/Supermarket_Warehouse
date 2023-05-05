import os.path
from Products import Products
from SuperMarket import SuperMarket
products = []
superMarkets = []
def EXISTS(code):
    for p in products:
        if p.get_code() == code:
            return True

    return False

def sEXISTS(code):
    for s in superMarkets:
        if s.get_code() == code:
            return True

    return False

def read_File(fname):
        with open(fname) as f:
            content_list = [line.split(";") for line in f]

        for x in content_list:
            code = x[0].strip()
            if EXISTS(code):
                print("The product {0} is repeated".format(code))
                exit()

            products.append(Products(x[0].strip(), x[1].strip(), x[2].strip(), x[3].strip(), x[4].strip(), x[5].strip()))



def printProducts():
    d = {}
    idx = 0
    for p in products:
        d[idx] = p
        idx += 1

    print("{:<25} {:<25} {:<25} {:<25} {:<25} {:<25}".format('Product Code', 'Product Name', 'Product Expiry Date', 'Product WholeSale Cost', 'Products Sale Cost',
                                 'Product Quantity'))
    for k, v in d.items():
        code = v.get_code()
        name = v.get_name()
        date = v.get_ex_date()
        wholesaleCost = v.get_wholesaleCost()
        saleCost = v.get_saleCost()
        quantity = v.get_quantity()
        print("{:<25} {:<25} {:<25} {:<25} {:<25} {:<25}".format(code, name, date, wholesaleCost, saleCost, quantity))




def printSuperMarkets():
    d = {}
    idx = 0
    for s in superMarkets:
        d[idx] = s
        idx += 1

    print("{:<25} {:<25} {:<25} {:<25}".format('SuperMarket Name', 'SuperMarket Code', 'SuperMarket Address', 'SuperMarket Added Date'))
    for k, v in d.items():
        code = v.get_code()
        name = v.get_name()
        date = v.get_date()
        address = v.get_address()
        print("{:<25} {:<25} {:<25} {:<25}".format(name, code, address, date))






def addSuperMarket():
    print("Enter the Info for the SuperMarket")
    scode = input("Enter the code of the Super Market: ")
    while True:
        if sEXISTS(scode):
            print("You have to insert a code that does not exist")
            scode = input("Enter the code of the Super Market: ")
        elif any(not c.isnumeric() for c in scode):
            print("CODE has to contain numbers (not characters)")
            scode = input("Enter numerical value for the code: ")
        else:
            break
    name = input("Enter the super market's name: ")
    okn = 0
    while okn == 0:
        if any(c.isnumeric() for c in name):
            print("You have to insert a name with characters (not numbers) ")
            name = input("Enter the super market's name: ")
            okn = 0
        else:
            okn = 1
    address = input("Enter the address of the super market: ")
    okc = 0
    while okc == 0:
        if not any(c.isalpha() for c in address):
            print("You have to insert an address with characters")
            address = input("Enter the address of the super market: ")
            okc = 0
        else:
            okc = 1
    date = input("Enter the added date of the super market: ")
    okd = 0
    while okd == 0:
        if any(c.isalpha() for c in date):
            print("You have to insert a date with numbers (not characters)")
            date = input("Enter the added date of the super market: ")
            okd = 0
        else:
            okd = 1

    print("The super market has been added successfully")
    adds = SuperMarket(name, scode, address, date)

    superMarkets.append(adds)
    printSuperMarkets()
    answer = input("do you want to add products to the supermarket? (Yes / No)")
    okh = 0
    while okh == 0:
        if answer.upper() != "Yes".upper() and answer.upper() != "No".upper():
            print("The answer has to be either Yes or No")
            answer = input("do you want to add products to the supermarket? (Yes / No)")
            okh = 0
        else:
            okh = 1
    if answer.upper() == "Yes".upper():
        code = input("Please enter the code of the product you want to add to the supermarket : ")
        quantity = input("Please enter the quantity of the product you want to add to the supermarket : ")
        ok = 0
        for p in products:
            if p.get_code() == code:
                ok = 1
                break
            else:
                ok = 0
        if ok == 1:
            for s in superMarkets:
                if s.get_code == scode:
                    s.productInS[scode] = code
                    print(s.productInS)
                    break
            print("The product has been added to the market successfully")
        else:
            print("Product not found in the store")


def addProduct():
    print("Enter the Info for the new product")
    code = input("Enter product code: ")
    while True:
        if EXISTS(code):
            print("You have to insert a code that does not exist")
            code = input("Enter product code: ")
        elif any(not c.isnumeric() for c in code):
            print("CODE has to contain numbers (not characters)")
            code = input("Enter numerical value for the code: ")
        else:
            break
    name = input("Enter the product's name: ")
    okn = 0
    while okn == 0:
        if any(c.isnumeric() for c in name):
            print("You have to insert a name with characters (not numbers) ")
            name = input("Enter the product's name: ")
            okn = 0
        else:
            okn = 1
    date = input("Enter product expiry date: ")
    okd = 0
    while okd == 0:
        if any(c.isalpha() for c in date):
            print("You have to insert a date with numbers (not characters)")
            date = input("Enter product's expiry date: ")
            okd = 0
        else:
            okd = 1
    wholesaleCost = input("Enter product's wholesale cost: ")
    okc = 0
    while okc == 0:
        if any(c.isalpha() for c in wholesaleCost):
            print("You have to insert a number (not characters) ")
            wholesaleCost = input("Enter product's wholesale cost: ")
            okc = 0
        else:
            okc = 1
    saleCost = input("Enter product's sale cost: ")
    okcc = 0
    while okcc == 0:
        if any(c.isalpha() for c in saleCost):
            print("You have to insert a number (not characters) ")
            saleCost = input("Enter product's sale cost: ")
            okcc = 0
        else:
            okcc = 1
    quantity = input("Enter product's quantity: ")
    okp = 0
    while okp == 0:
        if any(c.isalpha() for c in quantity):
            print("You have to insert product's quantity with numbers (not characters) ")
            quantity = input("Enter product's quantity: ")
            okp = 0
        else:
            okp = 1
    print("The product has been added successfully")
    addp = Products(code, name, date, wholesaleCost, saleCost, quantity)

    products.append(addp)
    printProducts()

def menu():
    print(70 * '-')
    print("Choose a number from 1 - 6 and 7 to exit")
    print("1- Add product items to the warehouse")
    print("2- Add a new supermarket to the management system")
    print("3- List of items in the warehouse based on expiry date")
    print("4- Clear an item from the warehouse")
    print("5- Distribute products from the warehouse to a supermarket")
    print("6- Generate a report about the sales status of the warehouse")
    print("7- Exit")
    print(70 * '-')
    n = int(input("\nEnter your choice: "))
    print()
    print(70 * '-')
    if n == 1:
        addProduct()
    elif n == 2:
        addSuperMarket()
    elif n == 3:
        print()
    elif n == 4:
        print()
    elif n == 5:
        print()
    elif n == 6:
        print()
    elif n == 7:
        exit()
    else:
        print("check the number if it is from 1 - 7")
    print(70 * '-')
    menu()


file_exists = os.path.exists('warehouse_items.txt')

if file_exists:
    read_File("warehouse_items.txt")
    menu()
else:
    print("File does not exists")


