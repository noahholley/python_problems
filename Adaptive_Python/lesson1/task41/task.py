sum = 0
allnums = []
squares = []

first = int(input())
allnums.append(first)
sum = sum + first

while sum != 0:
    first = int(input())
    allnums.append(first)
    sum = sum + first

for nums in allnums:
    squares.append(nums * nums)

for idx, nums in enumerate(squares):
    sum = sum + nums

print(sum)
