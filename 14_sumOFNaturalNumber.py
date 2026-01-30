def sum_of_natural_number(num):
    summ = 0
    for i in range(1,num + 1):
        summ += i
    return summ

num = int(input("enter the number: "))
print(sum_of_natural_number(num))