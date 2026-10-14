math = int(input("Enter mathematics marks (out of 100) :"))
eng = int(input("Enter English marks (out of 100) :"))
science = int(input("Enter Science marks (out of 100) :"))

total = 300
obtained = math + eng + science
percentage = (obtained /total)*100

if eng >= 40 :
    if  math >= 40 :
        if  science >=40:
              if percentage >=80 and percentage <=100:
                      print("Grade A")
                      print("Total Marks    :",total)
                      print("Obtained Marks :",obtained)
                      print("Percentage     :",percentage)
              elif percentage >=60 and percentage <80:
                      print("Grade B")
                      print("Total Marks    :",total)
                      print("Obtained Marks :",obtained)
                      print("Percentage     :",percentage)
              elif percentage >=50 and percentage <60:
                      print("Grade C")
                      print("Total Marks    :",total)
                      print("Obtained Marks :",obtained)
                      print("Percentage     :",percentage)

              else:
                  print("F")
        else :
               print("Science Subject fail")

    else:
          print("Math subject Fail")
else :
      print("English Subject ")
               
    
