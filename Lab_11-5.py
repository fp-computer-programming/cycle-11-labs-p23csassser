# Creator CS 2/9/2023

import datetime

# Create a list containing the day numbers for the next 5 days, starting with today
today = datetime.date.today()
day_date = [today.day + i for i in range(5)]

# Using a tuple, assign the 5 letters to variables that represent each day
thu, fri, mon, tue, wed = tuple("T F M T W")

# Print each variable to see what they equal
print(thu, day_date[1])
print(fri, day_date[2])
print(mon, day_date[3])
print(tue, day_date[4])
print(wed, day_date[0])
