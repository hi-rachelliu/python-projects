letter_counter = {}
fname = input("Enter your file name: ")
fhand = open(fname)
for line in fhand:
    for letter in line:
        letter = letter.lower()
        if letter.isalpha():
            letter_counter[letter] = letter_counter.get(letter, 0) + 1

# prints the letters in letter_counter in decreasing order of frequency
lst = []
for letter, freq in list(letter_counter.items()):
    lst.append((freq, letter))
lst.sort(reverse = True)
for freq, letter in lst:
    print (letter, freq)