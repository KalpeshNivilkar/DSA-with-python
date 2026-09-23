def search_insert_position(nums,target):
    n = len(nums)
    low = 0
    high = n - 1
    pos = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] >= target:
            pos = mid
            high = mid - 1
        else:
            low = mid + 1
    return pos

nums = [1,1,1,3,4,5,6,7,10,11]
target = 9

print(search_insert_position(nums,target))
        

def search_insert_space(nums,target):
    n = len(nums)
    low = 0
    high = n - 1
    pos = n

    while low <= high:
        mid = (low + high)// 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= target:
            pos = mid
            high = mid - 1
        else:
            low = mid + 1
    return pos

nums = [1,1,1,3,4,5,6,7,10,11]
target = 9
print(search_insert_space(nums,target))