def matrix_in_square_order(nums):
    row = len(nums)
    col = len(nums[0])

    top = 0
    left = 0
    right = col - 1
    bottom = row - 1
    result = []
    while top <= bottom and left <= right:
        for i in range(left,right + 1):
            result.append(nums[top][i])
        top += 1

        for i in range(top,bottom + 1):
            result.append(nums[i][right])
        right -= 1

        for i in range(right,left -1,-1):
            result.append(nums[bottom][i])
        bottom -= 1

        for i in range(bottom,top -1,-1):
            result.append(nums[i][left])
        left += 1
    return result

nums = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(matrix_in_square_order(nums))



