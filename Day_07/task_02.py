word = input("Enter the Sentence :")
count=0
for i in word:
  if i in "AEIOU" or i in "aeiou":
      count = count + 1

print(count)