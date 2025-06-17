print("welcome into reccursion series")    #Recursion एक ऐसी प्रक्रिया है जिसमें एक function खुद को ही call करता है।यानि, function अपने अंदर फिर से उसी function को बुलाता है।

# def factorial(n):
#     if n == 1:                 #base case:
#         return 1
#     else:
#         return n * factorial(n-1)                                 # factorial number example using recursion

# factorial(7)
# print(factorial(7))



def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n = fibonacci(n-1)+ fibonacci(n-2)

print(fibonacci(10))