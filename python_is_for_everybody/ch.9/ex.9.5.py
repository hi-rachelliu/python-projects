fname = input("Enter your file name: ")
try: 
    fhand = open(fname)
except FileNotFoundError:
    print(f"Your file {fname} can't be opened!")
    quit()
domain_counter = {}

for line in fhand:
    if '@' and 'From:' in line: 
        pos = line.find('@') + 1
        line = line[pos:].rstrip()
        domain_counter[line] = domain_counter.get(line, 0) + 1
print (domain_counter)