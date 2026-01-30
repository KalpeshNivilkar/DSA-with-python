def isArmstrongNumber(num):
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

print(isArmstrongNumber(153))