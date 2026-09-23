# def moveZero(arr):
#     j = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[i],arr[j] = arr[j],arr[i]
#             j += 1
#     return arr
# arr = [0,1,0,2,15]
# print(moveZero(arr))

def move_zero(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j],arr[j] = arr[j],arr[i]
            j += 1
    return arr
arr = [0,1,0,2,15]
print(move_zero(arr))
