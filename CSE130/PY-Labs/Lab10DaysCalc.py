# 1. Name:
#      Aidan Greenwood
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      This algorithm is designed to calculate the number of days 
#      between two entered dates.
# 4. What was the hardest part? Be as specific as possible.
#      This was a big step up in complexity from previous labs for me.
#      When I first read the set up lab I actually understood it for once
#      which made me feel confident, but this was way more complicated
#      than I thought it would be. I think the hardest part, was validation.
#      A lot of my time went to the functions at the beginning, and I 
#      really just wanted to make sure that they were well made.
# 5. How long did it take for you to complete the assignment?
#      3 hours 46min


# The leap year function.
    # This will calculate whether a given year is a leap year
    # so that later we can add full years to the calculator.
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


# Validation functions.
    # These check to see whether the date entered is valid.
    # It runs in a while loop so that the user is prompted
    # to enter it again if it was invalid.
def valid_day(prompt):
    valid = False
    day = 0

    while not valid:
        try:
            day = int(input(prompt))
            if 1 <= day <= 31:
                valid = True
            else:
                print("Invalid day.\n")

        except ValueError:
            print("You must enter an integer.\n")

    return day


def valid_month(prompt):
    valid = False
    month = 0
    while not valid:
        try:
            month = int(input(prompt))
            if 1 <= month <= 12:
                valid = True
            else:
                print("Invalid month.\n")

        except ValueError:
            print("You must enter an integer.\n")

    return month


def valid_year(prompt):
    valid = False
    year = 0
    while not valid:
        try:
            year = int(input(prompt))
            if 1753 <= year:
                valid = True
            else:
                print("Invalid year.\n")

        except ValueError:
            print("You must enter an integer.\n")

    return year


def valid_date(day, month, year):
    assert 1 <= month <= 12
    assert year >= 1753

    return 1 <= day <= days_in_month(month, year)


def valid_order(
        start_day, start_month, start_year,
        end_day, end_month, end_year):
    
    assert 1 <= start_month <= 12
    assert 1 <= end_month <= 12
    assert start_year >= 1753
    assert end_year >= 1753
    
    return (start_year, start_month, start_day) <= (end_year, end_month, end_day)

# The variables and inputs.
# Set their intitial value.
start_day = 0
start_month = 0
start_year = 0

end_day = 0
end_month = 0
end_year = 0

days_between = 0

dates_valid = False
# This loop will ensure the start is before the end date.
while not dates_valid:

    start_valid = False
    # This loop makes sure the date entered is possible.
    # For example 31st of Feb. is not possible, as there
    # arn't 31 days in Feb.
    while not start_valid:
        start_day = valid_day("Enter the start day: ")
        start_month = valid_month("Enter the start month: ")
        start_year = valid_year("Enter the start year: ")

        start_valid = valid_date(start_day, start_month, start_year)

        if not start_valid:
            print("Invalid: That month does not have enough days.\n")

    end_valid = False

    while not end_valid:
        end_day = valid_day("Enter the end day: ")
        end_month = valid_month("Enter the end month: ")
        end_year = valid_year("Enter the end year: ")

        end_valid = valid_date(end_day, end_month, end_year)

        if not end_valid:
            print("Invalid: That month does not have enough days.\n")

    dates_valid = valid_order(
        start_day, start_month, start_year, 
        end_day, end_month, end_year)
    
    if not dates_valid:
        print("Invalid: The end date can't be before the start date.\n")


# The full calculator function.
def days_calc(start_day, start_month, start_year,
              end_day, end_month, end_year):
    
    days_between = 0
    
    assert valid_date(start_day, start_month, start_year)
    assert valid_date(end_day, end_month, end_year)
    assert valid_order(start_day, start_month, start_year,
                       end_day, end_month, end_year)

    # Simplest solution: it's the same day.
    if (start_day == end_day and
        start_month == end_month and
        start_year == end_year):

        return 0
    
    # These will track the changes through the function.
    current_day = start_day
    current_month = start_month
    current_year = start_year

    # Next simplest: only the days are different
    if current_year == end_year and current_month == end_month:
        
        return end_day - current_day
    
    # Getting to this point means the other two 
    # if statements are false, meaning we can 
    # safely start changing the date drastically.

    # Finish the current month.
    days_between += days_in_month(current_month, current_year) - current_day

    current_month += 1

    if current_month > 12:
        current_month = 1
        current_year += 1

    # Finish starting year.
    if current_month != 1 and current_year < end_year:

        original_year = current_year
        while current_month != 1:
        
            days_between += days_in_month(current_month, current_year)

            current_month += 1

            if current_month > 12:
                current_month = 1
                current_year += 1
        
        assert current_year == original_year + 1
        assert current_month == 1

    # Add complete years to get to end year if necessary.
    while current_year < end_year:

        if is_leap_year(current_year):
            days_between += 366

        else:
            days_between += 365

        current_year += 1

    # Add months to get to end month if necessary.
    while current_month < end_month:

        days_between += days_in_month(current_month, current_year)

        current_month += 1
    
    # Add days to get to end day if necessary.
    days_between += end_day

    assert days_between >= 0
    return days_between


days = days_calc(start_day, start_month, start_year,
              end_day, end_month, end_year)

print(f"There are {days} days")