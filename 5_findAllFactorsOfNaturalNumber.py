def factorsOfNumber(num):
    if num < 0:
        print("this is negative number, enter another number")
        
    for i in range(1,num +1):
        if num % i == 0:
            print(i)
        
num = int(input("enter the number : "))
factorsOfNumber(num)