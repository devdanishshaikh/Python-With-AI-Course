Balance=0
while True:
  Menu=int(input("Enter your Choice(1 Add Money 2 Spend 3 Balance 4 Exit)"))
  if Menu==1:
    add_money=int(input("Add Amount :"))
    Balance=Balance+add_money
    print("Add Amount  :",add_money)
  elif Menu==2:
    spend_money=int(input("Enter Spend Amount :"))
    if spend_money < Balance:
      Balance -=spend_money
      print("Spend Amount:",spend_money)
    else:
      print("Invalid Amount")
  elif Menu==3:
    print("Balance :",Balance)
  else:
    print("Exit")
    break

