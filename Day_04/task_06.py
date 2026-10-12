

cost = float(input("Enter the cost of the item :"))
selling_price = float(input("Enter the selling price of the item :"))
if selling_price > cost:
    print("Profit")
    print("Profit Amount:", selling_price - cost)
else:
    if selling_price < cost:
        print("Loss")
        print("Loss Amount:", cost - selling_price)
    else:
        print("No Profit No Loss")