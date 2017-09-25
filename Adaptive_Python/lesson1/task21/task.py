import math as mt


def get_input(a):
    return a.split("/")


def give_output(a):
    return " ".join(a)


def f_s_c_f(a):
    inp = get_input(a)
    """code here"""
    out = []
    num = int(inp[0])
    den = int(inp[1])
    if num == 1:
        out.append(str(0))
        out.append(str(den))
        return give_output(out)
    if den == 0 or num == 0:
        out.append(str(0))
        return give_output(out)
    if num % den == 0:
            out = num / den
            return int(out)
    else:
        while num != 1 and den != 0:
            out.append(str(mt.floor(num/den)))
            num = num % den
            num, den = den, num
        return give_output(out)

print(f_s_c_f(input()))
