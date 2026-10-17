def rotatedMatrix(nums):
    row = len(nums)
    col = len(nums[0])

    result = [[0] * row for _ in range(col)]

    for i in range(row):
        for j in range(col):
            result[j][i] = nums[i][j]
    
    for el in result:
        el.reverse()
        
    for i in range(row):
        nums[i] = result[i]
           
    return nums  

nums = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(rotatedMatrix(nums))


# optimal solution

def rotateImage(nums):
    row = (len(nums))
    col = (len(nums[0]))

    for i in range(row):
        for j in range(i+1,col):
            nums[j][i],nums[i][j] = nums[i][j],nums[j][i]

    for i in range(row):
        nums[i].reverse()
    
    return nums
nums = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(rotateImage(nums))


def rotated_image(nums):
    row = len(nums)
    col = len(nums[0])

    for i in range(row):
        for j in range(i+1,col):
            nums[i][j],nums[j][i] = nums[j][i],nums[i][j]

    for i in range(row):
        nums[i].reverse()
    
    return nums
nums = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(rotated_image(nums))