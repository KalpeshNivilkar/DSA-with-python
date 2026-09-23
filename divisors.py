def divisors_of_num(num):
    divisors = []
    for i in range(1,int(num ** 0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)

    
    return sorted(divisors)
num = 36
print(divisors_of_num(num))