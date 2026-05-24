def floor_and_ceil(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    floor = -1
    ceil = -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return [nums[mid], nums[mid]]
        elif nums[mid] >= target:
            ceil =nums[mid]
            high = mid - 1
        else:
            floor = nums[mid]
            low = mid + 1
    return [floor,ceil]

nums = [1,1,1,3,4,5,6,7,10,11]
target = 9
print(floor_and_ceil(nums,target))