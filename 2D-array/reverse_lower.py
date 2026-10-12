nums = [[10,20,30],
        [40,50,60],
        [70,80,90]]
row = len(nums)
col = len(nums[0])
i = 0
for i in range(row):
    for j in range(col):
        if j <= col-i-1:
            print(nums[i][j], end=" ")
        else:
            print("*", end= " ")
    print()