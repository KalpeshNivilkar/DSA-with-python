# Question 1: Sorted Squared Array - You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.


# def sorted_squared_array(x):
#     new_array = []
#     for i in x:
#            i = i * i 
#            new_array.append(i)
#     new_array.sort()
#     return new_array

# arr = [10,20,40,57]
# print(sorted_squared_array(arr))


# def sorted_squared_array(x):
#     new_array = []
#     for i in x:
#         i = i * i
#         new_array.append(i)
#     new_array.sort()
#     return new_array

# arr = [10,20,30,40]
# print(sorted_squared_array(arr))
       
        
def square_arr(array):
    new_array =[]
    for i in array:
        i = i* i
        new_array.append(i)
    new_array.sort()
    return new_array

arr = [10,20,40,30]
print(square_arr(arr))
    