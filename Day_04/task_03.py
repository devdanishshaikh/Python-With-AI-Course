# Task:3 ask for number if it is negative turn into positive and Donot use abs()

num = int(input("Enter your Number :"))
print("Entered Number :",num)
if num < 0:
    num = -num
    print("Converted Number ",num)