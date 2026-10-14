temp = float(input("Enter the Temperature (Number) :"))
if temp <=0:
  print("ICE")
elif temp >0 and temp <=100:
  print("WATER")
else:
  print("STEAM")