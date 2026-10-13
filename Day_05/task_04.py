units = int(input("Enter the number of units consumed : "))

if units <= 100:
  bill = units * 10
  print(f"{units} units gives  {bill}")
elif units >=101 and units <= 200:
  bill = units * 15
  print(f"{units} units gives  {bill}")
else:
  bill = units * 20
  print(f"{units} units gives  {bill}")