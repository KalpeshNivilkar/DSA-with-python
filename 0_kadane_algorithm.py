# largest subarray sum using kadane algorithm 

# def max_subarray(nums):
#     currSum = 0
#     maxSum = float('-inf')  # start lower than any possible sum

#     for i in nums:
#         currSum += i
#         maxSum = max(maxSum, currSum)

#         if currSum < 0:
#             currSum = 0

#     return maxSum  


# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(max_subarray(arr))  
# Output: 6

# leetcode ans :

# class Solution(object):
#     def maxSubArray(self, nums):
#         currSum = 0
#         maxSum = float('-inf')

#         for i in nums:
#             currSum += i
#             maxSum = max(maxSum, currSum) 

#             if currSum < 0:
#                 currSum = 0

#         return maxSum  


# sol = Solution()          
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(sol.maxSubArray(arr))  



"""""def maxsum(num):
    cursum = 0
    maxsum = float('-inf')

    for i in num:
        cursum += 1
        maxsum = max(cursum,maxsum)

        if cursum == 0:
            cursum = 0
    return maxsum
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxsum(arr))  """""



def maxsum(num):
    cursum = 0
    maxsum = float('-inf')

    for i in num:
        cursum += 1
        maxsum = max(cursum,maxsum)

        if cursum < 0:
            cursum = 0
    return maxsum
arr = [10,22,-11,11,2,3]
print (maxsum(arr))