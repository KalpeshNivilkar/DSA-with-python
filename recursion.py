print("welcome into reccursion series")    #Recursion एक ऐसी प्रक्रिया है जिसमें एक function खुद को ही call करता है।यानि, function अपने अंदर फिर से उसी function को बुलाता है।

# def factorial(n):
#     if n == 1:                 #base case:
#         return 1
#     else:
#         return n * factorial(n-1)                                 # factorial number example using recursion

# factorial(7)
# print(factorial(7))


                                                   
# def fibonacci(n):                                              # fibonacci series
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         n = fibonacci(n-1)+ fibonacci(n-2)

# print(fibonacci(10))



# def factorial(num):                                             # factorial number
#     if num == 0:                                                # base case / condition if it is not present then recursion stack will overflow
#         return 0
#     elif num == 1:                                         
#         return 1
#     else:
#         return num * factorial(num-1)

# n = int(input("Enter any number : "))
# factorial(n)
# print(factorial(n))


# practice question 1] write a recursion function  to calculate the sum of first n number

# def calsum(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return num + calsum(num - 1)
# n= int(input("enter any number : "))
# print(calsum(n))


# practice question 2] Print numbers from n to 1

def rev_num(num):
    if num == 0:
        return 0
    print(num)
    rev_num(num-1)
    
n = int(input("enter any number : "))
print(rev_num(n))