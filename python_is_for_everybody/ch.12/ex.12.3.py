# Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, 
# (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the 
# document. Don't worry about the headers for this exercise, simply show the first 3000 characters
# of the document contents.

characters = 0

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    line = line.rstrip()
    words = line.decode()
    characters = characters + len(words)
    if characters < 3000:
        print (words)

print(characters)