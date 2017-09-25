def take_input(a):
    return a.split()


def print_output(a):
    for item in a:
        print(item)
    return


def fizz_buzzer(a):
    num_list = take_input(a)
    finished_list = []
    for item in range(int(num_list[0]), int(num_list[1]) + 1):

        if item % 3 == 0 and item % 5 != 0:
            finished_list.append("Fizz")
        elif item % 5 == 0 and item % 3 != 0:
            finished_list.append("Buzz")
        elif item % 5 == 0 and item % 3 == 0:
            finished_list.append("FizzBuzz")
        else:
            finished_list.append(item)
    return print_output(finished_list)

fizz_buzzer(input())

