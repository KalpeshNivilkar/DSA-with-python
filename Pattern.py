# simple pattern printing

# for i in range(3):
#     for j in range(2):
#         print("*",end="")
#     print("*")

# take input from user

# n = int(input())
# m = int(input())

# for row in range(n):
#     for column in range(m):
#         print(column,end="")
#     print("")


# num = 1
# for i in range(1,7):
#     for j in range(i):
#         print("*",end="")
#         num += 1
#     print()
   

# n = int(input())
# m = int(input())
# for i in range(n):
#     for j in range(m):
#         print(j,end="")
#     print(i)
   
# num = 1
# n =int(input())
# for i in range(1,n-1):
#     for j in range(i):
#         print("*",end="")
#     print("")



# for i in range(10):
#     print()

# size= 10
# for i in range(size):
#     print("*" * size)

# size= 5
# for i in range(size):
#     print("*" * (i+1))

# output
# *
# **
# ***
# ****
# *****


# size= 5
# for i in range(size):
#     print("*"*(size-i))


# output
# *****
# ****
# ***
# **
# *

# 1)

for i in range(0,4):
    for j in range(0,4):
        print("*",end=" ")
    print()

"""output : 
* * * * 
* * * * 
* * * * 
* * * *""" 

# 2)

for i in range(0,4):
    for j in range(0,i+1):
        print("*", end = " ")
    print()

"""output:
* 
* * 
* * * 
* * * * """

# 3)
for i in range(1,5):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
"""output:
1 
1 2 
1 2 3 
1 2 3 4"""


# 4)
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
"""output:
1 
2 2 
3 3 3 
4 4 4 4 """

# 5)
for i in range(0,5):
    for j in range(5-i):
        print("*",end=" ")
    print()

"""output:
* * * * * 
* * * * 
* * * 
* * 
* """
# 6)

for i in range(1,5):
    for j in range(5-i):
        print(j+1,end=" ")
    print()

"""output:
1 2 3 4 
1 2 3 
1 2 
1"""

# 7)

for i in range(0,5):
    for j in range(i+2):
        print(i,end=" ")
    print()
    