H = int(input())
A = int(input())
B = int(input())


def test(h, a, b):

    height = 0

    day = 1

    while True:
        height += a
        if height >= h:
            print(day)
            break
        height -= b
        day += 1

test(H, A, B)
