num_1 = float(input("Enter the First Number :"))
num_2 = float(input("Enter the Second Number :"))

operator = input("Enter the Operator (+, -, *, /) :")

if num_1 == 0 or num_2 == 0:
  print("Error: Division by zero is not allowed.")
else:
  if operator == "+":
      print(f"The sum of {num_1} and {num_2} is: {num_1 + num_2}")
  elif operator == "-":
    print(f"The difference of {num_1} and {num_2} is: {num_1 - num_2}")
  elif operator == "*":
    print(f"The product of {num_1} and {num_2} is: {num_1 * num_2}")
  elif operator == "/":
    print(f"The quotient of {num_1} and {num_2} is: {num_1 / num_2}")
  else:
    print("Invalid operator. Please use +, -, *, or /.")
