# brute force approach

def setZeros(matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                markInfinity(matrix, i, j)
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0

def markInfinity(matrix, row, col):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        if matrix[i][col] != 0:
            matrix[i][col] = float("inf")
    for j in range(c):
        if matrix[row][j] != 0:
            matrix[row][j] = float("inf")

matrix = [
    [1, 2, 0],
    [4, 5, 6],
    [7, 0, 9]
]

setZeros(matrix)
print(matrix)

# optimal approach

def setZeros(matrix):
    r = len(matrix)
    c = len(matrix[0])

    rowTrack = [0 for _ in range(r)]
    colTrack = [0 for _ in range(c)]

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                rowTrack[i] = -1
                colTrack[j] = -1
    
    for i in range(r):
        for j in range(c):
            if rowTrack[i] == -1 or colTrack[j] == -1:
                matrix[i][j] = 0

matrix = [
    [1, 2, 0],
    [4, 5, 6],
    [7, 0, 9]
]

setZeros(matrix)
print(matrix)