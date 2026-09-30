def runningSum(nums):
    n = len(nums)
    sum = 0
    total = []
    for i in range(n):
        sum += nums[i]
        total.append(sum)
    return total

nums= [10,20,30]
print(runningSum(nums))