def numberOfDigit(num):
    count = 0
    if num <= 0:
        return False
    while num > 0:
        
        num = num // 10
        count += 1
    return count
num = 23422
print(numberOfDigit(num))

