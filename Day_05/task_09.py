print("Should we Continue? (yes/no)")

x = input("Enter your choice (Yes/No): ")

if x == "yes" or x == "Yes" or x =="y" or x == "Y" or x == "YES":
    print("Continuing...")
elif x == "no" or x == "No" or x == "n" or x == "N" or x == "NO":
    print("Stopped...")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")