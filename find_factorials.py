def find_factoroals(num):
    fact = []
    for i in range(1,(int(num * 0.5)+1)):
        if num % i == 0:
            fact.append(i)
    return fact
num = 20
print(find_factoroals(num))