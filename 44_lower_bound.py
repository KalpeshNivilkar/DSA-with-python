# def findFloor(arr,k):
#     n = len(arr)
#     lb = -1               
#     low, high = 0, n - 1  

#     while low <= high:
#         mid = (low + high) // 2        

#         if arr[mid] <= k:
#             lb = mid                  
#             low = mid + 1              
#         else:
#             high = mid - 1             

#     return lb
# arr = [1, 2, 8, 10, 11]
# k = 9
# print(findFloor(arr,k))


def lower_bound(nums,target):
    n = len(nums)
    low = 0
    high = n - 1
    lb = -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb

nums = [2,4,5,6,7,8,10,13]
target = 9                                              

print(lower_bound(nums,target))

