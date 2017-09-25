line_one = input().split()
array_length = line_one[0]
possible_nums = line_one[1]
array_of_nums = input().split()
solution = []

for num in range(int(possible_nums)):
    solution.append(0)

for num in range(int(array_length)):
    solution[int(array_of_nums[num]) - 1] += 1

print(" ".join(str(x) for x in solution))
