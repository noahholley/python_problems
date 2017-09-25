import sys
time = 0
d = {}
c = {}

web_times = sys.stdin.readlines()
for web_time in web_times:
    data = web_time.split()
    if data[0] in d:
        d[data[0]] = (int(data[1]) + d[data[0]])
        c[data[0]] = (int(c[data[0]] + 1))
    else:
        d[data[0]] = int(data[1])
        c[data[0]] = int(1)

for item in d:
    print("%s\t%s" % (item.strip(" "), int(d[item] / c[item])))
#for item in c:
#    print("%s\t%s" % (item.strip(" "), c[item]))
