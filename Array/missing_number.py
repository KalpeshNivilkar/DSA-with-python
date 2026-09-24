# Example 1:

# Input: nums = [3,0,1]

# Output: 2

def missing_num(nums):
    n = len(nums)
    actual_sum = 0
    suppose_sum = 0
    for i in range(n):
        actual_sum += nums[i]

    for j in range(n+1):
        suppose_sum += j

    missing_nums = suppose_sum - actual_sum 
    return missing_nums

nums = [3,0,1,2,4]
print(missing_num(nums))


# brute force  approach
def missing_num1(nums):
    n = len(nums)
    for i in range(n + 1):
        if i not in nums:
            return i
nums = [3,0,1,2,4]
print(missing_num1(nums))