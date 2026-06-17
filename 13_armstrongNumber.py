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


def armstrong_num(num):
    n = len(str(num))
    power = n
    og_num = num
    sum = 0
    while num > 0:
        last_digit = num % 10
        sum += last_digit ** power
        num = num // 10
    if sum == og_num:
        return True
    return False
num = 153
print(armstrong_num(num))
        



# armstrong  number
def is_armstong_number(num):
    og_num = num
    arm = 0
    n = len(str(num))
    power = n

    while num > 0:
        last_digit = num % 10
        arm += last_digit ** n
        num = num // 10
    
    if og_num == arm:
        return True
    return False
num = 153
print(is_armstong_number(num))

