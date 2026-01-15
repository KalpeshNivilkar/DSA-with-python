'''def fibonacciNumber(num):#as a limit
    a = 0
    b = 1
    for i in range(1,num+1):
        c = a + b
        a = b
        b = c
        print(c)

fibonacciNumber(10)'''



def fibonacciNumber(num):
    if num <= 1:
        return num
    else:
        return fibonacciNumber(num - 1) + fibonacciNumber(num - 2)

print(fibonacciNumber(6))