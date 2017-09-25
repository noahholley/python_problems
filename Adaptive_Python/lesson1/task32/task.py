word = input().lower().replace(" ", "")
i = len(word)
for letter in word:
    if letter == word[i-1]:
        i -= 1
        continue
    else:
        print("no")
        break
if i == 0:
    print("yes")
