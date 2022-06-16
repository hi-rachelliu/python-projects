from datetime import datetime

age = int(input("enter your age: "))
name = input("enter your name: ")
current_year = datetime.now().year
year = current_year + 100 - age 
print(f"You will turn 100 in the year {year}")