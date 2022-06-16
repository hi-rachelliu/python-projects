def lcm():
    bigger = 1
    try: 
        a = int(input("enter your first positive integer: "))
    except ValueError:
        print("Error: are you sure that was a positive integer?")
    try: 
        b = int(input("enter your second positive integer: "))
    except ValueError:
        print("Error: are you sure that was a positive integer?")
    if a > b:
        bigger = a
    elif b > a: 
        bigger = b
    lcm = bigger
    while not (lcm % a == 0 and lcm % b == 0):
        lcm += 1
    print ("Your LCM: ", lcm)

lcm()