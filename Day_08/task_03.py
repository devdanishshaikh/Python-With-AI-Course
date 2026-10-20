while 1 >0:
  num = int(input("Enter any Number :"))
  count =0
  for i in range(1,num+1):
    value =int(input(f"Enter  value {i}:"))
    count = count + value
  print("Toatl Sum :",count)
  print("Average :", count/num)