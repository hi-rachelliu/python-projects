print("Welcome to area calculator!")
shape = input("shape name = ")

if shape.lower() == "rectangle":
    length = float(input("Length: "))
    width = float(input("Width: "))
    area = length * width
    print ("Area = ", area)
elif shape.lower () == "circle":
    radius = float(input("Radius: "))
    area = 2 * 3.14 * radius
    print ("Area = ", area)
elif shape.lower() == "square":
    side = float(input ("Side: "))
    area = side ** 2
    print ("Area = ", area)
elif shape.lower() == "triangle":
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = 0.5 * base * height
    print ("Area = ", area)
else:
    print ("Uh oh. Not available, like me, emotionally.")
