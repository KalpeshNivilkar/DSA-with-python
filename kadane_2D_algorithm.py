def max_sum_rectangle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')

    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            # Add current column to each row
            for i in range(rows):
                temp[i] += matrix[i][right]

            # Find max subarray sum for this column range
            current_sum = kadane(temp)
            max_sum = max(max_sum, current_sum)

    return max_sum

# Example
matrix = [
    [1, 2, -1],
    [-3, 4, 5],
    [2, -6, 3]
]

print("Maximum sum rectangle:", max_sum_rectangle(matrix))
