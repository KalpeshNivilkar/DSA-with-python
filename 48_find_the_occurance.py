def occurance(nums,target):
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i]== target:
            count += 1
       
    return count
nums = [1,2,2,2,3,4]
target = 2

print(occurance(nums, target))

def occurance(nums,target):
    n = len(nums)
    first = -1
    last = -1

    for i in range(n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    
    if first == -1:
        return 0
    
    return last-first + 1
nums = [1,2,2,2,3,4]
target = 2

print(occurance(nums, target))


# optimize
def lowerbound(nums,target):
    n = len(nums)
    lb = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb

def upperbound(nums,target):
    n = len(nums)
    ub = n
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    return ub

def occurance_optimize(nums,target):
    lb = lowerbound(nums,target)
    if lb == -1:
        return 0
    ub = upperbound(nums,target)
    return ub - lb 

nums = [1,2,2,2,3,4]
target = 2

print(occurance_optimize(nums, target))

