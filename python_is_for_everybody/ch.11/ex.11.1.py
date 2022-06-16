import re

regex = input("Enter your regular expression: ")
count = 0
fhand = open('mbox.txt')
for line in fhand:
    if re.search(regex, line):
        count += 1

print(f"mbox.txt had {count} lines that matched {regex} ")