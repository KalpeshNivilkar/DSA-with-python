# Lower triangle code 
nums = [[10,20,30],
        [40,50,60],
        [70,80,90]]

rows= len(nums)
cols = len(nums[0])

for i in range(rows):
    for j in range(cols):
        if j <= i:
            print(nums[i][j], end=" ")
        else:
            print("*", end=" ")
    print()