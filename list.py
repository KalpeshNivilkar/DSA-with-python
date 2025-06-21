# myList = [10,30,20,]

# # print(myList,type(myList))
# # print(len(myList))
# # print(myList[3])
# # myList.append(50)
# # print(myList)
# # myList.pop(2)
# # print(myList)
# myList.sort()
# print(myList)

# taking input from user  and do sum of user input
 
# n = int(input("enter how much element you want to store :"))
# list = []
# sum = 0
#                                                                                   # taking input from user and do sum of user input 
# for i in range(n):
#     num = int(input(f"enter elements :"))
#     list.append(num)
#     sum += num

# list.sort()
# print(list)
# print(sum)


# finding min and max from list

# n = int(input())
# mylist = input().split()

# for i in range(n):
#     mylist[i] = int(mylist[i])

# print(mylist)


# practical question 

# 1] wrie a prigram to  ask the user  to enter their three movies  and store items into the list 

# movies = []

# mov1 = input("enter 1st movie :")
# mov2 = input("enter 2st movie :")
# mov3 = input("enter 3st movie :")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)
    
# another way to append 

# movies = []

# movies.append(input("enter 1st movie :"))
# movies.append(input("enter 1st movie :"))
# movies.append(input("enter 1st movie :"))

# print(movies)

# 2] palidrone value check 

# checkList = [1,2,3,2,1]
# copyl = checkList.copy()
# copyl.reverse()
# print(copyl)

# if checkList == copyl:
#     print("this list is palindrome")
# else:
#     print("this list is not palindrome")

# 3] find largest number in list 

# list = [13,45,34,23]

# findLargestNumber = max(list)
# print(findLargestNumber)

# 4] Count how many times a number appears in a list.

# list = [1, 2, 2, 3, 2]

# countlist = list.count(2)
# print(countlist)
    

# 5] taking input for list from user and finding sum of the
# n = int(input("how much element you want take :"))
# mylist = []
# sum = 0
# for i in range(n):
#     num = int(input(f"enter the number :"))
#     mylist.append(num)
#     sum += num

# print(mylist)
# print(sum)
      

# 6] taking input from user and print min and max value 

n = int(input("how much element you wanna add :"))
myList = []

for i in range(n):
    num = int(input(f"enter the number : "))
    myList.append(num)

print(f" list is : {myList}")
maximum_Num = max(myList)
minimum_Num = min(myList)
print(f" maximum number is : {maximum_Num}")
print(f" minimum number is : {minimum_Num}")







