def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]       
        j = i - 1           

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   
            j -= 1

        arr[j + 1] = key   

    return arr

arr = [5, 3, 4, 1]
print(insertion_sort(arr))




def Insertion_sort(nums):
    n = len(nums)

    for i in range(1,n):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums
nums = [5, 3, 4, 1]
print(Insertion_sort(nums))