fhand = open('mbox-short.txt')
for sentence in fhand:
    sentence = sentence.rstrip().upper()
    print (sentence)