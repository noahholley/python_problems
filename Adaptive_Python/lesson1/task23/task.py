numbers = input().split()
big = int(numbers[0])
small = int(numbers[0])
for number in numbers:
    if int(number) > big:
        big = int(number)
    if int(number) < small:
        small = int(number)
print(str(big) + " " + str(small))
