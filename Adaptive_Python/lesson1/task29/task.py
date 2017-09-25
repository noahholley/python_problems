length = int(input())
sum = 0

for number in range(length):
    num = int(input())
    if num % 6 == 0:
        sum += num
print(sum)
