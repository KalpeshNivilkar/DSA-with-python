# # brute force
# def minimum(nums):
#     min_el = nums[0]
#     n = len(nums)

#     for i in range(n):
#         if nums[i] < min_el:
#             min_el = nums[i]
#     return min_el

# optimized approach nums = [3,4,5,1,2]

# optimize code using binary search
def minimum(nums):
    n = len(nums)
    low = 0
    high = n - 1
    mini = float('inf')

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= nums[high]:
            mini = min(nums[mid],mini)
            high = mid - 1
        else:
            mini = min(nums[low],mini)
            low = mid + 1
    
    return mini

nums = [4,5,6,7,0,1,2]

print(minimum(nums))
        
        
        
