def rotate_arr(arr):
    n = len(arr)
    temp = arr[n-1]
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = temp
    return arr

arr = [10,30,29,28,12]
print(rotate_arr(arr))





def rotate_array(nums):
    n = len(nums)
    temp = n -1
    for i in range(n-2,-1,-1):
        nums[i+1] = nums[i]
    nums[0] = temp


arr = [10,30,29,28,12]
print(rotate_arr(arr))