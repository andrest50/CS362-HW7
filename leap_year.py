def leap_year(year):
    if(year % 100 == 0):
        return "Not a leap year"
    elif(year % 4 == 0):
        return "Leap year"