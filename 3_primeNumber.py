# check if number is primem or not 

"""""def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(17))"""""



def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(23))

# check the nuber is prime or not 
def prime_number(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    return False
num = 36
print(prime_number(num))    



def prime(num):
    count = 0
    for i in range(1,int(num ** 0.5 + 1)):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    if count == 2:
        return True
    return False
num = 36
print(prime(num)) 
