address_counter = {}
fname = input("Enter your file name: ")
try: 
    fhand = open(fname)
except FileNotFoundError:
    print(f"Your file {fname} was not found. Try again!")
    quit()

hour_counter = {}
for line in fhand:
    words = line.split()
    if line.startswith('From') and len(words) > 2:
        hour = (words[5]).split(':')[0]
        hour_counter[hour] = hour_counter.get(hour, 0) + 1

lst = []
for (k, v) in list(hour_counter.items()):
    lst.append((k,v))
lst.sort()
for (k, v) in lst:
    print (f"hour: {k}, count number: {v}")