def isSortedAndRotate(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[(i+1)%n]:
            count += 1
    return count <= 1
arr = [3,4,5,1,2]
print(isSortedAndRotate(arr))
        