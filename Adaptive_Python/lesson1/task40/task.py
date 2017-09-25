integer = int(input())
divisors = []

for number in range(integer):
    if number != 0:
        if integer % number == 0:
            divisors.append(number)

if len(divisors) > 1:
    print(divisors[1])
else:
    print(integer)
