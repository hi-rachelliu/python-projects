fname = input("Enter your file name: ")
# put everything into try! remember to quit() the program!
try: 
    if fname == "na na boo boo":
        print("Never gonna give you up!")
        quit()
    fhand = open(fname)
except FileNotFoundError: 
    print("Error: no such file exists!")
    quit()
count = 0
for line in fhand:
    if line.startswith("Subject: "):
        count += 1
print(f"There were {count} subject lines in {fname}")
