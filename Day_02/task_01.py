name = input("Enter your name: ")
age = int(input("Enter your age: "))
hourly_rate = float(input("Enter your hourly rate: "))
hours_worked = float(input("Enter the number of hours worked: "))

print("_ _ _ Employee PayRoll Summary_ _ _")
print(f"Employee :{name} (Age :{age})")
print("Gross Salary : $",hourly_rate * hours_worked)