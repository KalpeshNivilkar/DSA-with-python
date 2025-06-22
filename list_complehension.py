# syntax of list - complehension 4
# myList = [ele for ele in range(n)]

# example 

myList = [ele for ele in range(5)]
print(myList)

# output will be :[0, 1, 2, 3, 4]

# taking as user input 

myList = [int(ele) for ele in input().split() ]
print(myList)

# output will be : [12, 45, 78, 32, 45, 75]

myList = [int(ele)*2 for ele in input().split() ]
print(myList)