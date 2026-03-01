


def rev_integer(num):
    sign = 1
    if num < 0:
        sign = -1
        num = -num
    rev_num = 0
    while num > 0:
        digit = num % 10
        rev_num = rev_num * 10 + digit
        num = num // 10
    rev_num = sign * rev_num
    if rev_num < -2**31 or rev_num > 2**31 - 1:
        return 0
    return rev_num
print(rev_integer(321))