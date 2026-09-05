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

days_left = 0

# Get the lenght to be translated.
valid_input = False

while not valid_input:
    try:
        days_left = int(input("What is the length of your streak? "))

        if days_left >= 0:
            valid_input = True
        else:
            print("Please enter a non-negative integer.\n")

    except ValueError:
        print("Please enter an integer.\n")

assert days_left >= 0


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


# The Year leangth check function.
    # This will calculate how many days are in a year.
def days_in_year(date_year):

    if is_leap_year(date_year) == True:
        return 366

    else:
        return 365
    

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
        return False, date_month, date_year, date_day
    
    date_day = days_in_month(date_month, date_year)

    assert valid_date(date_day, date_month, date_year)

    return True, date_month, date_year, date_day


# Calculator function
def start_date_calc(date_day, date_month,
                    date_year, days_left, 
                    rollback_month, days_in_year):

    valid = True

    # Same date case:
    if days_left == 0:
        assert valid_date(date_day, date_month, date_year)
        return f"{date_month}/{date_day}/{date_year}"

    # Same month and year case:
    if days_left < date_day:

        date_day = date_day - days_left
        days_left = 0

    else:

        # Remove the current partial month.
        # Then move to the last day of the previous month.
        days_left = days_left - date_day

        valid, date_month, date_year, date_day = rollback_month(
            date_month, date_year, date_day
        )

        # Remove full months until reaching December,
        # unless the answer is found before then.
        while valid and date_month != 12 and days_left >= date_day:

            days_left = days_left - date_day

            valid, date_month, date_year, date_day = rollback_month(
                date_month, date_year, date_day
            )

        # If the date is positioned at December,
        # remove as many full years as possible.
        while valid and date_month == 12 and days_left >= days_in_year(date_year):

            days_left = days_left - days_in_year(date_year)
            date_year = date_year - 1

            if date_year < 1753:
                valid = False

            if valid:
                assert valid_date(date_day, date_month, date_year)

        # Remove full months inside the final year.
        while valid and days_left >= date_day:

            days_left = days_left - date_day

            valid, date_month, date_year, date_day = rollback_month(
                date_month, date_year, date_day
            )

        # Remove the leftover days inside the final month.
        if valid and days_left > 0:

            date_day = date_day - days_left
            days_left = 0

    # Verify that the calculation produced a valid date.
    if valid:

        assert days_left == 0
        assert valid_date(date_day, date_month, date_year)

        return f"{date_month}/{date_day}/{date_year}"

    else:
        return "Invalid date"


# Display date as a solution
start_date = start_date_calc(date_day, date_month,
                    date_year, days_left, 
                    rollback_month, days_in_year)
print(f"Your streak started {start_date}")