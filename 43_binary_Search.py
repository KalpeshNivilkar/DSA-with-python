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
nums = [2, 5, 6, 4, 2, 3]
target = 6

sorted_nums = sorted(nums)
print(binary_search(sorted_nums, target))
