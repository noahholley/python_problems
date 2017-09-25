"""Input a single character and change its register.
That is, if the lowercase letter has been entered – make it uppercase, and vice versa.
Characters that are not Latin ones need to stay unchanged."""

import sys

character = sys.stdin.readline()

if character.isupper():
    changed_char = character.lower()
else:
    changed_char = character.upper()

sys.stdout.write(changed_char)
