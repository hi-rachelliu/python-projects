fname = input("Enter your file name: ")
try: 
    fhand = open(fname)
except FileNotFoundError: 
    print("Error!")
    quit()
sum, count = 0, 0
for line in fhand: 
    if line.startswith("X-DSPAM-Confidence:"):
        number = float(line[20:].strip())
        sum = sum + number
        count += 1
print (f"Average spam confidence: {sum/count}")