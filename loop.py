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

num = int(input())
i = 0
while i < num:
    if i%2 == 0:      
        print("0" , end="")
    else:
        print("*", end="")
    i += 1


       






