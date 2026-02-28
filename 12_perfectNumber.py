"""def perfectNumber(num):
    result = 0
    for i in range(1,num):
        if num % i == 0:
            result += i
        
    if result != num:
        return False
    return True
print(perfectNumber(6))"""



def perfectNum(num):
    result = 0
    for i in range(1,num):
        if num % i == 0:
            result += i

    if result == num:
        return True
    return False

print(perfectNum(15))