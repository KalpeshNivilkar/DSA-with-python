'''Given an integer array nums, find the subarray with the largest sum, and return its sum.

 Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.'''

def maximum_subarray(nums):
    curr_sum = 0
    max_sum = float('-inf')

    for i in range(len(nums)):
        curr_sum += nums[i]
        max_sum = max(curr_sum, max_sum)

        if curr_sum < 0:
            curr_sum = 0
    return max_sum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maximum_subarray(nums))
    
