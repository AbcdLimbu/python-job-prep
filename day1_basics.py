import datetime

name = input("What is your name? \n")
try:
    age = int(input("How old are you? \n"))
except ValueError:
    print("Please enter a valid number for age.")
    exit()

currentYear = datetime.datetime.today().year
birthYear = currentYear - age

with open("data.txt", "w") as file:
    file.write(f"Name: {name} \nAge: {age} \nBirth Year: {birthYear}")

print("\nSaved Data:")
with open("data.txt", "r") as file:
    print(file.read())