"""def perfectNumber(num):
    result = 0
    for i in range(1,num):
        if num % i == 0:
            result += i
        
    if result != num:
        return False
    return True
print(perfectNumber(6))"""



"""def perfectNum(num):
    result = 0
    for i in range(1,num):
        if num % i == 0:
            result += i

    if result == num:
        return True
    return False

print(perfectNum(15))"""



def perfectnumber(num):
    if num == 1:
        return False
    sum = 1
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            sum += i + num // i
        return sum == num
print(perfectnumber(15))