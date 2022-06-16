address_counter = {}
fname = input("Enter your file name: ")
try: 
    fhand = open(fname)
except FileNotFoundError:
    print(f"Your file {fname} was not found. Try again!")
    quit()

# method #1
for line in fhand:
    words = line.split()
    if line.startswith('From') and len(words) > 2:
        address_counter[words[1]] = address_counter.get(words[1], 0) + 1
print (address_counter)

""" 
method #2:
for line in fhand:
    words = line.split()
    if line.startswith('From') and len(words) > 2:
        if words[1] not in address_counter: 
            address_counter[words[1]] = 1
        else:
            address_counter[words[1]] += 1
print (address_counter)
"""