name = input("enter your first and last name: ")
names = name.split(' ')
first = names[0] 
last = names[1]
for letter in first: 
    new_first = first[::-1]
for letter in last:
    new_last = last[::-1]
print (new_first, new_last)