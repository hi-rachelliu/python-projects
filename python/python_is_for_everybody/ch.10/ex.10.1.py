# old code from ex.9.3
address_counter = {}
fname = input("Enter your file name: ")
try: 
    fhand = open(fname)
except FileNotFoundError:
    print(f"Your file {fname} was not found. Try again!")
    quit()

for line in fhand:
    words = line.split()
    if line.startswith('From') and len(words) > 2:
        address_counter[words[1]] = address_counter.get(words[1], 0) + 1

# creates new list, reverses order of the list
lst = []
for email, count in list(address_counter.items()):
    lst.append((count, email))
lst.sort(reverse = True)
for mail, count in lst[:1]:
    print (mail, count)