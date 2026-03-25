"""def isArmstrongNumber(num):
    summ = 0
    order = len(str(num))
    temp = num   # store original value

    while temp > 0:
        digit = temp % 10
        summ += digit ** order
        temp //= 10

    return summ == num

print(isArmstrongNumber(153))

def isArmstrongNumber(num):
    summ = 0
    order = len(str(num))
    temp = num

    while temp > 0:
        digit = temp % 10
        summ += digit ** order
        temp //= 10
    
    return summ == num

print(isArmstrongNumber(153))
    


def isArmstrongNumber(num):
    summ = 0
    power = len(str(num))
    temp = num

    while temp > 0:
        digit = temp % 10
        summ += digit ** power
        temp //= 10
    return(summ == num)

print(isArmstrongNumber(153))"""


def armstrong_num(num):
    og_num = num
    sum = 0
    power = len(str(num))
    if num <= 0:
        return False
    while num > 0:
        digit = num % 10
        sum = sum + digit ** power
        num = num // 10
    if og_num == sum:
        return True
    return False
num = 371
print(armstrong_num(num))
