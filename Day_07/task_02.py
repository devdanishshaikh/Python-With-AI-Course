word = input("Enter the Sentence :")
count=0
for i in word:
  if i in "AEIOUaeiou":
      count = count + 1

print("Total Vowel In word :", count)