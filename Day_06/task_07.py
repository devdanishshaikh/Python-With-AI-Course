data_used =int(input("Enter Data Used :"))


designation = input("Are You Student (Yes/No) :")

print(f"{data_used} GB")

if designation == "Yes":
    if data_used > 0 and data_used <=5:
        print(f"RS {500*(10/100)}")
    elif data_used >5 and data_used <=20:
        print(f"RS {1200*(10/100)}")
    else:
        print(f"RS {2000*(10/100)}")

else:
  if data_used > 0 and data_used <=5:
    print("RS 500")
  elif data_used >5 and data_used <=20:
    print("RS 1200")
  else:
    print("RS 2000")