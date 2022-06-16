# Change the socket program socket1.py to prompt the user for the URL so it can read 
# any web page. You can use split('/') to break the URL into its component parts so 
# you can extract the host name for the socket connect call. Add error checking 
# using try and except to handle the condition where the user enters an improperly 
# formatted or non-existent URL.

import socket

# wname = input("Enter your webpage: ")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\\r\\n\\r\\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(),end='')

mysock.close()

# Prints: 
# HTTP/1.1 200 OK
# Date: Sun, 14 Mar 2010 23:52:41 GMT
# Server: Apache
# Last-Modified: Tue, 29 Dec 2009 01:31:22 GMT
# ETag: "143c1b33-a7-4b395bea"
# Accept-Ranges: bytes
# Content-Length: 167
# Connection: close
# Content-Type: text/plain

# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief