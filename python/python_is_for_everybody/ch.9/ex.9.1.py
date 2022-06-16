fhand = open('words.txt')
dict = {}
for line in fhand:
    words = line.split()
    for word in words:
        dict[word] = dict.get(word, 0) + 1
print (dict)

if 'python' in dict:
    print ("True")
else:
    print ("False")