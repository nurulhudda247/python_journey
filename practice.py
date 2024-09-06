import string

user_input = input("Please enter a string: ")

uppercase = ""
lowercase = ""
digits = ""
punctuation = ""

for text in user_input:
    if text.isupper():
        uppercase += text
    elif text.islower():
        lowercase += text
    elif text.isdigit():
        digits += text
    else:
        punctuation += text

print("UPPERCASE: ", uppercase)
print("lowercase: ", lowercase)
print("Digits: ", digits)
print("Punctuations: ", punctuation)



# Check Palindrome Word
input_text = input("Enter a text to check Palindrome word: ").strip().lower()
reversed_text = input_text[::-1]
if reversed_text == input_text:
    print(input_text, "is a palindrome word")
else:
    print(input_text, "is not a palindrome word")