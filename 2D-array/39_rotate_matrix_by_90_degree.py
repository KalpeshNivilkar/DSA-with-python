'''def rotatedMatrix(nums):
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
print(rotated_image(nums))'''



# brute-force-approach
def rotate_matrix(nums):
    n = len(nums)
    rows = len(nums)
    cols = len(nums[0])

    result = [([0]* rows) for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][n-1-i] = nums[i][j]

    return result

nums = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(rotate_matrix(nums))


# optima solution 
def rotate(matrix):
        
    n = len(matrix)
    row = len(matrix)
    col = len(matrix[0])

    # inline_transpose
    for i in range(row):
        for j in range(i+1,col):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
    for i in range(row):
        matrix[i].reverse()
   
    return matrix
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

print(rotate(matrix))