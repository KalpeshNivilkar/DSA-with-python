def findFloor( arr, k):
    n = len(arr)
    lb = -1               # floor index; -1 means no floor yet
    low, high = 0, n - 1  # binary-search boundaries

    while low <= high:
        mid = (low + high) // 2        # middle index

        if arr[mid] <= k:
            lb = mid                   # potential (better) floor
            low = mid + 1              # look on the right side
        else:
            high = mid - 1             # look on the left side

    return lb
arr = [1, 2, 8, 10, 11]
k = 9
print(findFloor(arr,k))
