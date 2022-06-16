fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        words = line.split()
        count += 1
        print(words[1])
print (f"There are {count} lines that start with 'from'")