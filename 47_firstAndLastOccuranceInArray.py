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



def fristandlast(nums,target):
    n = len(nums)
    low = 0
    high = n - 1
    first = -1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            high = mid - 1
        else:
            low = mid + 1
        for i in range(n):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        
        return [first,last]

nums = [1,2,2,2,3,4]
target = 2

print(fristandlast(nums, target))
    

                
            

       
      
        
