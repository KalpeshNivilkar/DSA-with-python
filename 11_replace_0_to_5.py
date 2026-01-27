def replace_zero_to_five(num):
    if num == 0:
        return 5
    return int(str(num).replace('0','5'))

print(replace_zero_to_five(1020))


# without using the methods of string

"""def replace_zero_to_five(num):
    if num == 0:
        return 5
    
    result = 0
    place = 1

    while num > 0:
        digit = num % 10
        if digit == 0:
            digit = 5
    
        result += digit * place
        place *= 10
        num //= 10
    return result

print(replace_zero_to_five(1020))"""



def replace_number(num):
    if num == 0:
        return 5
    
    result = 0
    place = 1

    while num > 0:
        digit = num % 10
        if digit == 0:
            digit = 5
        result += digit * place
        place *= 10
        num //= 10
    return result
print(replace_number(1000))