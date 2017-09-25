def IsPointArea(x, y):
    circleX = -1
    circleY = 1
    circleR = 2


    if (x - circleX)**2 + (y - circleY)**2 <= circleR**2 and x + y >= 0 and y >= (2*x) + 2:
        return "YES"
    if (x - circleX)**2 + (y - circleY)**2 >= circleR**2 and x + y <= 0 and y <= (2*x) + 2:
        return "YES"
    else:
        return "NO"

    """if x + y > 0:
        print("point is above negative line")
    if x + y < 0:
        print("point is bellow negative line")
    if x + y == 0:
        print("point is on negative line")

    if y > (2*x) + 2:
        print("point is above positive line")
    if y < (2*x) + 2:
        print("point is bellow positive line")
    if y == (2*x) + 2:
        print("point is on positive line")"""

print(IsPointArea(int(input()), int(input())))
