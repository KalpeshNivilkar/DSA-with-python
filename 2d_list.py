matrix = [
  [1, 2, 3],   # row 0
  [4, 5, 6],   # row 1
  [7, 8, 9]    # row 2
]
rows = len(matrix)
cols = len(matrix[0])

# printing each elements of matrix 
print("all el:")
for i in range(0,rows):
    for j in range(0,cols):
        print (matrix[i][j])
    
# printing the sum of matrixes
print("this is sum :")
sum = 0
for i in range(0,rows):
    for j in range(0,cols):
        sum += matrix[i][j]
print(sum)

# print as matrix row * column
print("this is matrix :")
for i in range(0,rows):
    for j in range(0,cols):
        print(matrix[i][j],end=" ")
    print()

# print upper traingle
print("this is upper traingle:")
for i in range(0,rows):
    for j in range(0,cols):
        if j <= i:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

# print lower traingle
print("this is lower traianle:")

for i in range(0,rows):
    for j in range(0,cols):
        if j >= i:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

# print diagonal
print("this is diagonal:")

for i in range(0,rows):
    for j in range(0,cols):
        if j == i:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()

# print reverse diagonal
print("this is reverse diagonal:")
for i in range(0,rows):
    for j in range(0,cols):
        if j == cols - 1 - i:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()