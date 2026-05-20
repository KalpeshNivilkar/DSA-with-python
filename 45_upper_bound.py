def upperBound(arr, k):
    n = len(arr)
    up = n
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > k:
            up = mid
            high = mid - 1
        else:
            low = mid + 1

    return up


arr = [1, 2, 4, 4, 5, 7]
k = 4

print(upperBound(arr, k))


def upper_bound(nums,target):
    n = len(nums)
    low = 0
    high = n - 1
    up = n

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            up = mid
            high = mid - 1
        else:
            low = mid + 1
    return up

nums = [1,2,2,2,2,3,3,3,3,4,5,6,7,8]
target = 2

print(upper_bound(nums,target))
