"""def sumOfDigit(num):
    digitSum = 0
    for i in str(num):
        digitSum += int(i)
    return digitSum

def addDigit(num):
    while(len(str(num)) != 1):
        num = sumOfDigit(num)
    return num

print(sumOfDigit(382))"""


def sumOfDigit(num):
    summ = 0
    for i in str(num):
        summ += int(i)
    return(summ)

def addDigit(num):
    while(len(str(num)) != 1):
        num = sumOfDigit(num)
    return num
print(sumOfDigit(272))


    
