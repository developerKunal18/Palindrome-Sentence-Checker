import re

text = input("Enter sentence: ")

clean_text = re.sub(r'[^A-Za-z0-9]', '', text).lower()

if clean_text == clean_text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
