#!/usr/bin/python3
# This mdule prints the number of time a word occurs in a sentence
print("Input a word: ", end="")
string = input()
word_list = []
for i in string:
    if i not in word_list:
        word_list.append(i)
        count = string.count(i)
        print (f"{i} occurs {count} times")
    else:
        continue

