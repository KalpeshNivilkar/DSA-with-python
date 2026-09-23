def firstAndLastOccInSortedArray(nums,target):
    n = len(nums)
    first = -1
    last = -1

    for i in range(0,n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
            
    return [first,last]

nums = [1,2,2,2,3,4]
target = 2

print(firstAndLastOccInSortedArray(nums, target))



