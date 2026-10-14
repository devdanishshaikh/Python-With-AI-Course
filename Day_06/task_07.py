data_used =int(input("Enter Data Used :"))


designation = input("Are You Student (Yes/No) :")

print(f"{data_used} GB")

if designation == "Yes":
    if data_used > 0 and data_used <=5:
        discount = 500 *(10/100)
        price = 500 - discount
        print(f"Discount  RS {discount}")
        print(f"Price  RS {price}")
    elif data_used >5 and data_used <=20:
        discount = 1200 *(10/100)
        price = 1200 - discount
        print(f"Discount  RS {discount}")
        print(f"Price  RS {price}")
    else:
        discount = 2000 *(10/100)
        price = 2000 - discount
        print(f"Discount  RS {discount}")
        print(f"Price  RS {price}")

else:
  if data_used > 0 and data_used <=5:
    print("RS 500")
  elif data_used >5 and data_used <=20:
    print("RS 1200")
  else:
    print("RS 2000")