import sys

character = sys.stdin.readline()

if character.isupper():
    changed_char = character.lower()
else:
    changed_char = character.upper()

sys.stdout.write(changed_char)
