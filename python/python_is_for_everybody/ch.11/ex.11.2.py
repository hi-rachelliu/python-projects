import re

rev = []
rev_ave = 0
rev_temp = []

fname = input('Enter file: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    quit()

for line in fhand:
    line = line.rstrip()
    rev_temp = re.findall('^New Revision: ([0-9.]+)', line)
    for val in rev_temp:
        val = float(val)            # Convert the strings to floats
        rev = rev + [val]           # Add all values into list rev

rev_sum = sum(rev)
count = float(len(rev))
if count:
    rev_ave = rev_sum / count
print(rev_ave)