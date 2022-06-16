week_counter = {}
fname = input("Enter a file name: ")
try: 
    fhand = open(fname)
except FileNotFoundError:
    print(f"Error: {fname} can't be opened!")
    quit()

"""
method #1:
for line in fhand:
    words = line.split()
    if line.startswith('From') and len(words) > 3:
        if words[2] not in week_counter: 
            week_counter[words[2]] = 1
        else: 
            week_counter[words[2]] += 1
print (week_counter)
"""

# method #2:
for line in fhand:
    words = line.split()
    if line.startswith('From') and len(words) > 3:
        key = words[2]
        week_counter[key] = week_counter.get(key, 0) + 1
print (week_counter)