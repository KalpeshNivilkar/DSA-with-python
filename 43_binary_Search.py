def binary_search(nums, target):
    """Binary search in a sorted array.

    Returns the index of target if found, otherwise -1.
    """
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example (binary search requires a sorted array)
nums = [2,3,5,7,8,10]
target = 6


print(binary_search(nums, target))
