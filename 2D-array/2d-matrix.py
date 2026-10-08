# create a 2d matrix
matrix = [[10,20,30],
          [40,50,60],
          [70,80,90]]

rows = len(matrix)
col = len(matrix[0])

# print(rows,col)

# how to iterate 2d matrix 
for i in range(rows):
    for j in range(col):
        print(matrix[i][j])

