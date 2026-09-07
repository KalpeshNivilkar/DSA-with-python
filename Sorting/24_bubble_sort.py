"""def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr    
arr = [10,23,12,43,55,22]
print(bubble_sort(arr))"""


#bubble sort
def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n- i- 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [10,39,22,40,12]
print(bubble_sort(nums))

# done



def bubble(nums):
    n = len(nums)

    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums
nums = [10,19,20,11]
print(bubble(nums))





def buuible_sort2(nums):
    n = len(nums)
    for i in range(n -1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums
nums = [10,19,20,11]
print(buuible_sort2(nums))



def bu(nums):
    n = len(nums)

    for i in range(n - 1):
        for j in range(n - i -1):
            if nums[j] > nums[j +1]:
                nums[j], nums[j +1] = nums[j +1], nums[j]

    return nums
nums = [10,19,20,11]
print(bu(nums))
