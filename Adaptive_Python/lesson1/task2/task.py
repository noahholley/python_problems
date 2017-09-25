import sys

def is_leap_year(year):
    if year % 4 != 0:
        return "Regular"
    elif year % 100 != 0:
        return "Leap"
    elif year % 400 != 0:
        return "Regular"
    else:
        return "Leap"

print(is_leap_year(int(sys.stdin.read())))

