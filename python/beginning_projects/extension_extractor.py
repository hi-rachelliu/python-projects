fname = input("enter your file name: ")
position = fname.find ('.') + 1
print (position)
print (fname[position:])
if position == 0: 
    print("Error: are you sure what you entered has an extension?")