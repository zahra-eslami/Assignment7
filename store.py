import qrcode

PRODUCTS = []

def choice(ch):
    if ch == 1:
        Add()
    elif ch == 2:
        Edit()
    elif ch == 3:
        Remove()
    elif ch == 4:
        Search()
    elif ch == 5:
        Show_list()
    elif ch == 6:
        Buy()
    elif ch==7:
        code = input("please enter your code: ")
        generate_qr_code(code)
    elif ch == 8:
        write_to_database()
        save_to_file()
        exit(0)
    else:
        print("Your choice is not in the list, please choose again")
        Show_menu()

def Show_menu():
    print('1 -> Add')
    print('2 -> Edit')
    print('3 -> Remove')
    print('4 -> Search')
    print('5 -> Show Menu')
    print('6 -> Buy')
    print('7 -> Generate QR Code')
    print('8 -> Exit')

def read_from_database():
    with open('Assignment7/database.txt', 'r') as f:
        for line in f:
            result = line.split(",")
            my_dictionary = {
                "code": result[0],
                "name": result[1],
                "price": result[2],
                "count": result[3].strip()  # Remove newline character
            }
            PRODUCTS.append(my_dictionary)

def Add():
    code = input("Enter code: ")
    name = input("Enter name: ")
    price = input("Enter price: ")
    count = input("Enter count: ")
    new_product = {'code': code, 'name': name, 'price': price, 'count': count}
    PRODUCTS.append(new_product)

def Edit():
    code = input("Enter the product code: ")
    for product in PRODUCTS:
        if product["code"] == code:
            print("Select the field to edit:")
            print("1- Name")
            print("2- Price")
            print("3- Count")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                new_name = input("Enter the new name: ")
                product["name"] = new_name
            elif choice == 2:
                new_price = input("Enter the new price: ")
                product["price"] = new_price
            elif choice == 3:
                new_count = input("Enter the new count: ")
                product["count"] = new_count
            else:
                print("Invalid choice.")
                return
            print("Information updated successfully.")
            return
    print("Product not found.")

def Remove():
    code = input("Enter the product code to remove: ")
    for product in PRODUCTS:
        if product["code"] == code:
            PRODUCTS.remove(product)
            print("Product successfully removed.")
            return
    print("Product not found.")

def generate_qr_code(code):
    for product in PRODUCTS:
        if product["code"] == code:
            file_name = product["name"]+"\n" + product["price"]+"\n"+product["count"]
            name=product["name"]
            img_QR = qrcode.make(file_name)
            type(img_QR)
            img_QR.save(name+".png")
            print("Your product QR code successfully generated8")
 
            break
    else:
        print("product not found!")


def Search():
    user_input = input("Enter user keyword: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print("code \t\t  name  \t\t price")
            print("-" * 50)
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"], "\t\t \n")
            break
    else:
        print("Not found.")

def Show_list():
    print("code \t\t  name  \t\t price")
    print("-" * 50)
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"], "\t\t")

def Buy():
    while True:
        code = input("Enter the product code: ")
        for product in PRODUCTS:
            if product["code"] == code:
                quantity = int(input("Enter quantity: "))
                if int(product["count"]) >= quantity:
                    product["count"] = str(int(product["count"]) - quantity)
                    print("Product added to cart.")
                else:
                    print("Insufficient stock.")
                break
        else:
            print("Product not found.")
        choice = input("Do you want to buy more products? (y/n): ")
        if choice.lower() != 'y':
            break

def write_to_database():
    with open('Assignment7/database.txt', 'w') as f:
        for product in PRODUCTS:
            f.write(f"{product['code']},{product['name']},{product['price']},{product['count']}\n")

def save_to_file():
    with open('data_backup.txt', 'w') as f:
        for product in PRODUCTS:
            f.write(str(product) + "\n")

print('Welcome to Py Store 🛒')
read_from_database()
print('Loading... Data is loaded successfully.')

while True:
    Show_menu()
    choice(int(input('Enter your choice: ')))
