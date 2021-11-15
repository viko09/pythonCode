month = int(input('Type a number from 1 to 12, please'))

while month < 1 or month > 12:
    print("Please choose a number from 1 to 12.")
    month = int(input('Type a number from 1 to 12, please'))

if month == 12 or month == 1 or month == 2:
    print(f"The season for month {month} is Winter.")
elif month == 3 or month == 4 or month == 5:
    print(f"The season for month {month} is Spring.")
elif month == 6 or month == 7 or month == 8:
    print(f"The season for month {month} is Summer.")
else:
    print(f"The season for month {month} is Autum.")
