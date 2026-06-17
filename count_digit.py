# count digit

def count_digit(num):
    freq = 0
    n = num

    while n > 0:
        last_digit = n % 10
        print(last_digit)
        freq += 1
        n = n // 10
    return freq
num = 121
print(count_digit(num))