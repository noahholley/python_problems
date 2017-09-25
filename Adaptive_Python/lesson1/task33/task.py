import math as mt

cs = int(input())
bio = int(input())
gcd = mt.gcd(cs, bio)

if gcd == 1:
    print(int(cs * bio))
else:
    print(int(cs * bio / gcd))
