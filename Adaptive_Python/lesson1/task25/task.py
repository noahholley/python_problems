import re

p = re.compile("19 \d \d \d \d \d \d \d \d\d")
c = re.compile("19\d{9}")
number = input()
if bool(p.search(number)) | bool(c.search(number)) and len(number) == 11:
    print("Yes")
else:
    print("No")
