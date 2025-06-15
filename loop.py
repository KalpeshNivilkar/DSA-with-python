# for loop using range

# for i in range(5):
#     print(i)

# printing sum of numbers using for
# num = int(input())
# sum = 0
# for i in range(num):
#     sum += i+1
#     print(sum)


# num = int(input())
# for i in range(num):
#    if i%2==0:
#                             #  here end="" used for continue in horizontal line
#       print("0",end="")      
#    else:
#                             #  here end="" used for continue in horizontal line
#       print("*", end="")





# while loop                   # in while loop at the end line of code should determine the increment

# num = int(input())
# i = 0
# while i < num:
#     if i%2 == 0:      
#         print("0" , end="")
#     else:
#         print("*", end="")
#     i += 1


# Q1 Print numbers from 1 to 10 using a loop.

# for i in range(1,10):
#     print(i)

# Q2 Print even numbers between 1 to 50.

# for i in range(50):
#     if i%2 == 0:
#      print(i)
       
# Q3 Print the multiplication table of a number entered by the user.

# n = int(input())

# for i in range(n):
#    print(i*i)
       
#  Q4 Calculate the sum of first n natural numbers.

# n = int(input())
# sum = 0

# for i in range(n):
#     sum+=i
#     print(sum)

# Q5 Print a square pattern of stars (e.g. 5x5 * grid).

# size = 5
# for i in range(size):
#     print("*" * (size) )
       
# Q6 Print only odd numbers from 1 to 20

# for i in range(10):
#     if i%3 == 0:
#         print(i)

# Q7 Print the reverse of numbers from 10 to 1.
 
# for i in range(10,0,-1):
#     print(i)

# by taking input from user

n=int(input())

for i in range(n,0,-1):
    print(i)






