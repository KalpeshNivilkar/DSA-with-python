def perfectNumber(num):
    
    result = 0
    for i in range(1,num):
        if num % i == 0:
            result += i
        
    if result != num:
        return False
    return True
print(perfectNumber(6))

