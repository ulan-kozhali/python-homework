years = int(input("Enter number of years: "))

days = years*365
weeks = years*52
months = years*12
hours = (years*365)*24

day = input("If you want to see number of days, press 1: ")
def show_days (days, weeks, months, hours):
    if int(day) == 1:
        print(f"Number of days: {days}")
    else:
        print ()
show_days (days, weeks, months, hours)

week = input("If you want to see number of weeks, press 2: ")
def show_weeks (days, weeks, months, hours):
    if int(week) == 2:
        print (f"Number of weeks: {weeks}")
    else:
        print ()
show_weeks (days, weeks, months, hours)

month = input("If you want to see number of months, press 3: ")
def show_month (days, weeks, months, hours):
    if int(month) == 3:
        print (f"Number of months: {months}")
    else:
        print ()
show_month (days, weeks, months, hours)

hour = input("If you want to see number of months, press 4: ")
def show_hour (days, weeks, months, hours):
    if int(hour) == 4:
        print (f"Number of hours: {hours}")
    else:
        print ()
show_hour (days, weeks, months, hours)