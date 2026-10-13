print("*********Enter your Detail and marks************")
name = input("Enter your name                       : ")
university = input("Enter your university           : ")
campus_location = input("Enter your campus location : ")
dept = input("Enter your department                 : ")
roll_no = input("Enter your roll number             : ")
age = int(input("Enter your age                     : "))
marks = int(input("Enter your marks                 : "))
print("***********************************************")



marks = 75

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("========= Student Detail ============")
print("Name                 : ", name)
print("University           : ", university)
print("Campus Location      : ", campus_location)
print("Department           : ", dept)
print("Roll Number          : ", roll_no)
print("Age                  : ", age)
print("Marks                : ", marks)
print("Grade                : ", grade)
print("=====================================")
