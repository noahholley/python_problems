import re
import sys

for line in sys.stdin:
    if re.search(r'\b([c][a][t])\b', line):
        print(line[:-1])
