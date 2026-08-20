# num = 1234
# n = num
# while n > 0:
#     last_digit = n % 10
#     print(last_digit)
#     n = n // 10




def extraction_of_digit(num):
    # num = nums
    while num > 0:
        last_digit = num % 10
        print(last_digit)
        num = num // 10

nums = 123
print(extraction_of_digit(nums))

