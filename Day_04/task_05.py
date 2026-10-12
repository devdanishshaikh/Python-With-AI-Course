#Ask for whole number divisble by both print both print only 3 and 5 neither print neither

num = float(input("Enter a whole number :"))
if num % 3 == 0 and num % 5 == 0:
  print("Both")
else:
  if num % 3 == 0:
    print("Only by 3")
  else:
    if num % 5 == 0:
      print("Only by 5")
    else:
      print("Neither") 