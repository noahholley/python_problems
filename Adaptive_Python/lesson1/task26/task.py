a = int(input())
b = int(input())
c = int(input())

s = (a+b+c)/2
d = (s-a) * (s-b) * (s-c)

if d > 0:
    print("YES")
else:
    print("NO")


