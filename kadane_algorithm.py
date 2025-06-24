# def max_subarray(nums):
#      currSum = 0
#      maxSum = float('-inf') 

#      for i in nums:
#           currSum += i
#           maxSum = max(maxSum,currSum)

#           if currSum < 0:
#                currSum = 0
    
    
# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print(max_subarray(arr))




def max_subarray(nums):
    currSum = 0
    maxSum = float('-inf')  # start lower than any possible sum

    for i in nums:
        currSum += i
        maxSum = max(maxSum, currSum)

        if currSum < 0:
            currSum = 0

    return maxSum  # <-- return the result!

# Test it:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(arr))  # Output: 6
