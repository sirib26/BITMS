def zellers_formula(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    
    # Century and year of the century
    C = year // 100
    Y = year % 100
    
    # Zeller's formula
    h = (day + (13 * (month + 1)) // 5 + Y + Y // 4 + C // 4 + 5 * C) % 7
    
    # Convert h to day of the week
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_of_week = days_of_week[h]
    
    return day_of_week

# Take input from the user
day = int(input("Enter the day (1-31): "))
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year (e.g., 2024): "))

if day<0 or month<0 or year<0:
    print("negative value")
    exit()
elif day<1 or day>31:
    print(" day not in range")
    exit()
elif month<1 or month>12:
    print("month not in range")
    exit()
elif year<1900 or year>9999:
    print("year not in range")
    exit()

'''if not all(isinstance(value, int) for value in (day, month, year)):
    print("Invalid output")
else:
    day_input = int(day)
    month_input = int(month)
    year_input = int(year)
    print("Input is valid. Day: {}, Month: {}, Year: {}".format(day, month, year))'''

    
# Call the function and print the result
day_of_week = zellers_formula(day, month, year)
print("The day of the week for {}/{}/{} is: {}".format(day, month, year, day_of_week))
