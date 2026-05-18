num = 9876353552
count = 0

n = num
while n > 0:
    last_digit = n % 10
    count += 1
    n = n // 10
print(count)
