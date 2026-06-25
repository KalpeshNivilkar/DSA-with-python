# def factorsOfNumber(num):
#     if num < 0:
#         print("this is negative number, enter another number")
        
#     for i in range(1,num +1):
#         if num % i == 0:
#             print(i)
        
# num = int(input("enter the number : "))
# factorsOfNumber(num)




def all_divisors(num):
    divisor = []
    if num <= 0:
        return False
    for i in range(1,(int (num * 0.5) +1)):
        if num % i == 0:
            divisor.append(i)
    return divisor

num = 36
print(all_divisors(num))       


def factorials(nums):
    list = []
    
    for i in range(1,(int(nums * 0.5) + 1)):
        if nums % i == 0:
            list.append(i)
    return list

nums = 28
print(factorials(nums))

# find all factors of number

def find_factors(num):
    list = []
    for i in range(num):
        if num % i == 0:
            list.append(i)
    return list
nums = 28
print(factorials(nums))


def find_factors(num):
    list = []
    for i in range(1,(int(num * 0.5)+ 1)):
        if num % i == 0:
            list.append(i)
    return list
num = 28
print(find_factors(num))


