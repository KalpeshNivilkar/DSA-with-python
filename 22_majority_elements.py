# brute-forse approach

def majorityElement(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                count += 1
        
        if count > len(nums)// 2:
            return nums[i]
        
nums = [1,2,1,2,3,1,1,1,1,1]
print(majorityElement(nums))


def mEl(nums):
    d = dict()
    for i in range(len(nums)):
        if i in d[nums]:
            d[nums[i]] += 1
        else:
            d[nums[i]] = 1
    return d
nums = [1,2,1,2,3,1,1,1,1,1]
print(mEl(nums))

