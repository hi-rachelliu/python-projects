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
print (address_counter)

# counts the most common address and its count number

big_count = 0
for address in address_counter:
    if big_count < address_counter[address]:
        big_address = address
        big_count = address_counter[address]
print (big_address, big_count)
