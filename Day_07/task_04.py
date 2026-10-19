word = input("Enter the Sentence: ")

reversed = ""

for i in word:
    reversed = i + reversed

if reversed == word:
    print("Palindrome")
    print("Reversed:", reversed)
else:
    print("Not a palindrome")
    print("Reversed:", reversed)