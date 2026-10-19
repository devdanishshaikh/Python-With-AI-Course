print("============================================")
print("\t\tWELCOME TO FOOD PALACE")
print("=============================================")

customer_name = input("Enter Customer Name :")

print("----------------- MENU ------------------------")

print("1. Fast Foood")
print("2. Pakistani Food")
print("3. Cold Drinks")

Menu = int(input("Enter Category : "))

if Menu == 1:
    print("---------------Fast food---------------------")
    item_1 = "Burger"
    item_2 = "Pizza"
    item_3 = "Fries"
    Burger = 500
    Pizza  = 1200
    Fries  = 300
    print(f"1. Burger      RS. {Burger}")
    print(f"2. Pizza      RS. {Pizza}")
    print(f"3. Fries      RS. {Fries}")
    item =int(input("Enter Item :"))
    if item == 1:
        print("You have Selected :Burger")
        print(f"Price : RS .{Burger}")
    elif item == 2:
        print("You have Selected :Pizza")
        print(f"Price : RS .{Pizza}")
    elif item == 3:
        print("You have Selected :Fries")
        print(f"Price : RS .{Fries}")
    else:
        print("Invalid item")
elif Menu == 2:
    print("---------------Pakistani food---------------------")
    item_1 = "Biryani"
    item_2 = "Karahi"
    item_3 = "Nihari"
    Biryani = 500
    Karahi  = 1200
    Nihari  = 300
    print(f"1. Biryani      RS. {Biryani}")
    print(f"2. Karahi      RS. {Karahi}")
    print(f"3. Nihari      RS. {Nihari}")
    item =int(input("Enter Item :"))
    if item == 1:
        print("You have Selected :Biryani")
        print(f"Price : RS .{Biryani}")
    elif item == 2:
        print("You have Selected :Karahi")
        print(f"Price : RS .{Karahi}")
    elif item == 3:
        print("You have Selected :Nihari")
        print(f"Price : RS .{Nihari}")
    else:
        print("Invalid item")

elif Menu == 3:
    print("---------------Cold Drinks food---------------------")
    item_1 = "Coke"
    item_2 = "Pepsi"
    item_3 = "Water"
    Coke = 150
    Pepsi  = 150
    water  = 80
    print(f"1. Coke      RS. {Coke}")
    print(f"2. Pepsi      RS. {Pepsi}")
    print(f"3. Water      RS. {water}")
    item =int(input("Enter Item :"))
    if item == 1:
        print("You have Selected :Coke")
        print(f"Price : RS .{Coke}")
    elif item == 2:
        print("You have Selected :Pepsi")
        print(f"Price : RS .{Pepsi}")
    elif item == 3:
        print("You have Selected :Water")
        print(f"Price : RS .{water}")
    else:
        print("Invalid item")
else:
    print("Invalid Category")
        
quantity = int(input("Enter Quantity :"))

if Menu ==1:
    if item ==1:
        price = Burger
        Sub_price =quantity * Burger
    elif item == 2:
        price = Pizza
        Sub_price =quantity * Pizza
    elif item == 3:
        price =  Fries
        Sub_price = quantity * Fries
elif Menu == 2:
    if item == 1:
        price =Biryani
        Sub_price = quantity * Biryani
    elif item == 2:
        price =Karahi
        Sub_price = quantity * Karahi
    elif item == 3:
        price =Nihari
        Sub_price = quantity * Nihari
elif Menu == 3:
    if item == 1:
        price =Coke
        Sub_price = quantity * Coke
    elif item == 2:
        price =Pepsi
        Sub_price = quantity * Pepsi
    elif item == 3:
        price = water
        Sub_price = quantity * water

print("-----------------------------------------------------------")

print("Customer Type ")
print("1. Student")
print("2. Regular")
print("3. VIP")  

print("-----------------------------------------------------------")

cutomer_type = int(input("Enter Customer Type :"))

if cutomer_type == 1:
    discount = price * 0.10
    print("Student Discount : 10%")
elif cutomer_type == 2:
    print("Regular Customer")
    discount = price * 1
elif cutomer_type == 3:
    print("VIP Customer Discount : 20%")
    discount = price * 0.20
   
else:
    print("Invalid Customer Type")

print("-----------------------------------------------------------")

print("Payment Method ")
print("1. Cash")
print("2. Credit Card")
print("3. Debit Card")

print("-----------------------------------------------------------")

cash_method = int(input("Enter Payment Method :"))

if cash_method == 1:
   print("Cash Service Charge : RS. 0")
   service_charge = 0
   print(f"Service Charge : RS. {service_charge}")
   final_price = (Sub_price + service_charge)-discount
elif cash_method == 2:
    print("Credit Card Service Charge : RS. 2%")
    service_charge = discount * 0.02 
    final_price = (Sub_price + service_charge)-discount
elif cash_method == 3:
    print("Debit Card Service Charge : RS. 1%")
    service_charge = discount * 0.01
    final_price = (Sub_price + service_charge)-discount
else:
    print("Invalid Payment Method")



print("============================================================")
print("\t\t\tFiINAL BILL")
print("============================================================")

print(f"Customer Name        : {customer_name}")
print(f"Item Price           : RS. {price}")
print(f"Quantity             : {quantity}")
print(f"Sub Total            : RS. {Sub_price}")
print(f"Discount             : RS. {discount}")
print(f"Service Charge       : RS. {service_charge}")
print(f"Final Price          : RS. {final_price}")

print("============================================================")