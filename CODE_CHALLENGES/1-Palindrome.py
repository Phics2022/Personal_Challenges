#!/usr/bin/python3
# this module checks if a string is a palindrome

print("Input a text: ", end="")
text = str(input())
if len(text) == 0:
    exit()
text_reverse = text[-1: :-1]
if text == text_reverse:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
