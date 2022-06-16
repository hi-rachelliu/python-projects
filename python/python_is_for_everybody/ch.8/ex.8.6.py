lst = []
while True:
    n = input("Number: ")
    if n == 'done':
        break
    try: 
        float(n)
    except ValueError:
        print("Error!")
        quit()
    lst.append(n)
    
print(f"Max: {max(lst)}")
print(f"Min: {min(lst)}")