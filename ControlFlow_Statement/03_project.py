'''RESTURENT MENU PROJECT '''

print("\t\t\t WELCOME TO OUR RESTURENT")
print("Choose the food type:\n1.Breakfast\n2.Lunch\n3.Dinner")

food = input("Enter your food:").lower()

if food == "breakfast":
    print("\t\t\t------MENU------")
    print("-"*30)
    print("1.Idli : 10 RS\n2.Dosa : 15 RS\n3.Pongal : 30 Rs\n4.Puri : 20 RS\n5.Vada : 5 RS")
    print("-"*30)

    item = input("Enter your item: ").lower()
    if item == "idli":
        quantity = int(input("Enter the quantity:"))
        total_bill = 10 * quantity
    elif item == "dosa":
        quantity = int(input("Enter the quantity:"))
        total_bill = 15 * quantity
    elif item == "Pongal":
        quantity = int(input("Enter the quantity:"))
        total_bill = 30 * quantity
    elif item == "Puri":
        quantity = int(input("Enter the quantity:"))
        total_bill = 20 * quantity
    elif item == "Vada":
        quantity = int(input("Enter the quantity:"))
        total_bill = 5 * quantity
    else:
        print("This Breakfast item is not available")


elif food == "lunch":
    print("\t\t\t------MENU------")
    print("-"*30)
    print("1.Chicken Biryani : 150 RS\n2.Round Meal : 90 RS\n3.Veg Biryani : 70 Rs\n4.Curd Rice : 50 RS\n5.Lemon Rice : 30 RS")
    print("-"*30)

    item = input("Enter your item: ").lower()
    if item == "chicken biryani":
        quantity = int(input("Enter the quantity:"))
        total_bill = 150 * quantity
    elif item == "round meal":
        quantity = int(input("Enter the quantity:"))
        total_bill = 90 * quantity
    elif item == "veg biryani":
        quantity = int(input("Enter the quantity:"))
        total_bill = 70 * quantity
    elif item == "curd rice":
        quantity = int(input("Enter the quantity:"))
        total_bill = 50 * quantity
    elif item == "lemon rice":
        quantity = int(input("Enter the quantity:"))
        total_bill = 30 * quantity
    else:
        print("This Lunch disc is not available")


elif food == "dinner":
    print("\t\t\t------MENU------")
    print("-"*30)
    print("1.Chapati : 15 RS\n2.Parota : 20 RS\n3.Fried Rice : 120 Rs\n4.Idiyopam : 10 RS\n5.Naan : 20 RS")
    print("-"*30)

    item = input("Enter your item: ").lower()
    if item == "chapati":
        quantity = int(input("Enter the quantity:"))
        total_bill = 15 * quantity
    elif item == "parota":
        quantity = int(input("Enter the quantity:"))
        total_bill = 20 * quantity
    elif item == "fried rice":
        quantity = int(input("Enter the quantity:"))
        total_bill = 120 * quantity
    elif item == "idiyopam":
        quantity = int(input("Enter the quantity:"))
        total_bill = 10 * quantity
    elif item == "naan":
        quantity = int(input("Enter the quantity:"))
        total_bill = 20 * quantity

    else:
        print("This Dinner disc is not available")

else:
    print("Sorry Your Item is not available")

print("\t\t\t BILL")
print("-"*50)
print(f"Your Item : {item}")
print(f"Your Quantity : {quantity}")
print(f"Total Bill : {total_bill}")
print("-"*50)
print("\t\t\t Thank You Visit Again")



    


