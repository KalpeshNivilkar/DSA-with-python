def rev_num(num):
    rev = 0
    if num <= 0:
        return False
    
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev
num = 8373863
print(rev_num(num))
        