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
 
n = int(input("enter how much element you want to store :"))
list = []
sum = 0
                                                                                  # taking input from user and do sum of user input 
for i in range(n):
    num = int(input(f"enter elements :"))
    list.append(num)
    sum += num

list.sort()
print(list)
print(sum)


# finding min and max from list

# n = int(input())
# mylist = input().split()

# for i in range(n):
#     mylist[i] = int(mylist[i])

# print(mylist)
