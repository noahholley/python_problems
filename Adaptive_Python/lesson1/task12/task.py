weekdays = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
leave=input()
d=int(input())
l = weekdays.index(leave)
# l is the numeric version of which day
# d is the number of days until return
r = d % 7 - (7 - l)

# Enter your formula for calculating the return day

print("If you leave on {} and return {} days later, you will return on {}.".format(leave,d,weekdays[r]))
