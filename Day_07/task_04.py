while 1 >0:
  print("========================Check the word is Palindrome or Not==================")
  word = input("Enter the Sentence: ")

  reversed = ""

  for i in word:
    reversed = i + reversed

  if reversed == word:
    print("Palindrome")
    print("Reversed:", reversed)
    print("===============================END===========================================")
  else:
    print("Not a palindrome")
    print("Reversed:", reversed)
    print("===============================END===========================================")