# # *dictionary : are used to store data in key:value pairs 
# # method 1 : key()
# # method 2 : values()


# # for example 
# myInfo = {
#     "key":"value",
#     "name":"kalpesh",
#     "age": 21,
#     "add":"gokulnagar",
#     "sub":["python","c","C++"]

# }
# print(myInfo)

# print(myInfo.keys())

# print(myInfo.values())


# # practise question 

# dict = {"table": ["a piece of furniture","list of fact and figure"],
#         "cat":"a small animal"}

# print(dict)

# # practise question 

# n = int(input("hoow much sub store :"))
# dict = {}
# for i in range(n):
#     sub = input("enter the sub :")
#     marks = input("enter the marks :")
#     dict[sub] = marks
# print(dict)

n = int(input("how much sub you have to store"))

dict = {}
for i in range(n):
    sub = input("enter the sub ")
    marks = input("enter the marks ")

    dict[sub] = marks
print(dict)

for avarageMarks in marks:
    print([marks])
