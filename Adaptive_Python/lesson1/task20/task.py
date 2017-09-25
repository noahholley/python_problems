inp = int(input())
a = 1
b = 0
for num in range(inp):
    b = b + a
    a = a / -2
print(b)
