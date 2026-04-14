
def findMaxConsecutiveOnes(nums):
    count = 0
    max_count = 0

    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count

nums = [1,1,1,1,0,0,1,1,1,1,0,1,0]
print(findMaxConsecutiveOnes(nums))



def find_1(arr):
    count = 0
    maxcount = 0
    for i in range(0,len(arr)):
        if arr[i] == 1:
            count += 1
            maxcount = max(maxcount,count)
        else:
            count = 0
    return maxcount
arr = [1,1,1,1,0,0,1,1,1,1,0,1,0]
print(find_1(arr))
