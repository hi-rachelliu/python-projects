# greatest common divisor
def gcd(): 
    try:
        a = int(input("enter your first positive number: "))
    except ValueError:
        print("This is not a positive integer.")
    try: 
        b = int(input("enter your second second number: "))
    except ValueError:
        print("This is not a positive integer.")
    gcd = 1
    bigger = 1
    if a > b:
        bigger = a
    elif a < b: 
        bigger = b
    for i in range (bigger, 1, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    print (gcd) 

gcd()