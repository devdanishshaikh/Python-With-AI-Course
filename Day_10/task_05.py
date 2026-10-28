count =0
while True:
  print("1 add 2 show 3 Exit")
  choice=int(input("Enter choice: "))
  if choice=="1":
    count+=1
  elif choice=="2":
    print("Count is: "+(count))
  elif choice=="3":
    break
  else:
    print("Invalid choice")