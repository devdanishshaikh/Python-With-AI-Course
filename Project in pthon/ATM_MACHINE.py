print("======================================================")
print("\t WELCOME TO HBL BANK ATM DADU SINDH")
print("======================================================")

balance = 5000
password = input("Enter PIN :")
count=0
while password != "admin@123":
  count+=1
  if count == 3:
    print("Card Blocked Due to 3 wrong Attempts.")
    exit()
  print("Invalid PIN. Please try again.")
  password = input("Enter PIN :")
while True:
  if password == "admin@123":
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit Money")
    print("4. Change PIN")
    print("5. EXIT")

  choice = int(input("Enter your choice: "))
  if choice == 1:
    print("Your Balance is: ", balance)
    print("====================================================")
  elif choice == 2:
    withdraw_amount = int(input("Enter amount to withdraw: "))
    if withdraw_amount <= balance:
      balance -= withdraw_amount
      print("Withdrawal successful. New balance is: ", balance)
      print("====================================================")
    else:
      print("Insufficient funds.")
      print("=====================================================")
  elif choice == 3:
    deposit_amount = int(input("Enter amount to deposit: "))
    balance += deposit_amount
    print("Deposit successful. New balance is: ", balance)
    print("=====================================================")
  elif choice == 4:
    new_pin = input("Enter new PIN: ")
    password = new_pin
    print("PIN changed successfully.")
    print("=====================================================")
  elif choice == 5:
    print("Thank you for using HBL BANK ATM.")
    print("=====================================================")
    exit()

print("======================================================")
