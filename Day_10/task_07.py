while True:
  choice =int(input("Enter Your Choice(1 KM 2 Kg 3 Exit) :"))
  if choice==1:
    Km=int(input("Enter Distance :"))
    miles=Km*0.621
    print(f"Distance :{miles} miles")
  elif choice==2:
    kg=int(input("Enter Weight :"))
    pounds=kg*2.205
    print(f"Weight :{pounds} pounds")
  elif choice==3:
    print("Exit")
    break
  else:
    print("Invalid Choice")

