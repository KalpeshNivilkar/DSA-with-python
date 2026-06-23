# brute force approach
def searchInRotateArray(nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    
    return -1

nums = [4, 5, 6, 0, 1, 2]
target = 0

print(searchInRotateArray(nums, target))
       

# optimized approach
def searchInSortedArray(nums,target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1

nums = [4, 5, 6, 0, 1, 2]
target = 0

print(searchInRotateArray(nums, target))




            