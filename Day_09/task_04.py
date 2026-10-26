size_of_square = int(input("Enter the Size the of Square :"))
for i in range(size_of_square):
  for j in range(size_of_square):
    if i == 0 or i == size_of_square-1 or j == 0 or j == size_of_square-1:
      print(" ", end="\t")
    else:
      print(" ", end="\t")
  print("\n")