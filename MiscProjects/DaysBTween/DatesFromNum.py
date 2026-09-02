"""
Aidan Greenwood

The purpous of this program is to take an intiger
input, streak leangth, then return the start date
from the current day.
"""

from datetime import date

# Get the current date.
today = date.today()

date_month = today.month
date_day = today.day
date_year = today.year

streak_length = 0

# Get the lenght to be translated.
valid_input = False
while not valid_input:
    try:
        streak_length = int(input("What is the length of your streak? "))
        
        if streak_length >= 0:
            valid_input = True
        else: print("Please enter a positive intiger.\n")

    except ValueError:
        print("Please enter an integer.\n")

    assert streak_length >= 0
    days_left = streak_length


# Helper functions -
# The leap year function.
    # This will calculate whether a given year is a leap year
    # so that later we can subtract full years in the calculator.
def is_leap_year(year):
    # This only works after 1752 when the Gregorian calendar took effect.
    # Anything before that is invalid. If this fires, then add code for
    # the Julian calendar.
    assert(year > 1752)

    # Not a leap year if not evenly divisible by 4
    if year % 4 != 0:
        return False

    # A leap year if not divisible by 100
    if year % 100 != 0:
        return True

    # Only centuries are left
    if year % 400 == 0:
        return True
    else:
        return False
    

# The month checker function.
    # This will check to see how many days are in a month.
def days_in_month(month, year):
    assert 1 <= month <= 12
    assert year > 1752
    # This accounts for Feb. during leap.
    if month == 2:

        if is_leap_year(year):
            return 29
        else:
            return 28
        
    elif month in [4, 6, 9, 11]:
        return 30
    
    else:
        return 31
    
# The valid date function.
    # This ensurs the output of the calculator is valid.
def valid_date(day, month, year):
    assert 1 <= month <= 12
    assert year >= 1753

    return 1 <= day <= days_in_month(month, year)


# Rollback and year verification function.
    # Rolls back months and years, as well as
    # validates them.
def rollback_month(date_month, date_year, date_day):

    date_month = date_month - 1

    if date_month == 0:
        date_month = 12
        date_year = date_year - 1

    if date_year < 1753:
        return False
    
    date_day = days_in_month(date_month, date_year)

    assert valid_date(date_day, date_month, date_year)

    return True, date_month, date_year, date_day


# Calculator function

    # Same date case:

    # Same month and year case:

    # Begin bigger calculation.
        # Remove the current partial month.
        # Then move to the last day of the previous month.


        # Remove full months until reaching December,
        # unless the answer is found before then.


        # If the date is positioned at December,
        # remove as many full years as possible.


        # Remove full months inside the final year.


        # Remove the leftover days inside the final month.


# Display date as a solution
print(date_month)