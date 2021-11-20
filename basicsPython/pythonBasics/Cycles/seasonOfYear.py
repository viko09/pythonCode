month = int(input('Type a number from 1 to 12, please'))

while month < 1 or month > 12:
    print("Please choose a number from 1 to 12.")
    month = int(input('Type a number from 1 to 12, please'))

if month == 12 or month == 1 or month == 2:
    print(f"The season for month {month} is Winter.\n")
elif month == 3 or month == 4 or month == 5:
    print(f"The season for month {month} is Spring.\n")
elif month == 6 or month == 7 or month == 8:
    print(f"The season for month {month} is Summer.\n")
else:
    print(f"The season for month {month} is Autum.\n")

age = int(input('Type an age, please'))

while age < 0 or age > 140:
    print("Please type your age again.")
    age = int(input('Type an age, please'))

if 0 >= age or age <= 10:
    print(f"The life is starting...")
elif 11 >= age or age <= 20:
    print(f"A lot of changes and study...")
elif 21 >= age or age <= 30:
    print(f"You are in the apogees of your life...")
else:
    print(f"Enjoy your life, because you might die soon.")
