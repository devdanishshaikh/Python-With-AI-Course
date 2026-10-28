while True:
  choice =int(input("1 Hello 2 Bye 3 Exit :"))
  if choice==1:
    print("Hello!")
    
  elif choice ==2:
    print("Good Bye")
  elif choice==3:
    print("Exit")
    break
  else:
    print("Invalid Choice")