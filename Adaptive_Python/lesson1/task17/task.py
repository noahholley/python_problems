seconds = int(input())
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
while h >= 24:
    h -= 24
print("%d:%02d:%02d" % (h, m, s))
