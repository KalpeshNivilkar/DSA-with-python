'''"""def largestEl(arr):
    j = 1
    for i in range(len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j]= arr[j],arr[i]
            j += 1
    return arr[i]
arr = [55,32,97,99,3,67]
print(largestEl(arr))"""

def largestEl(arr):
    largest = 0
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest
arr = [55,32,97,99,3,67]
print(largestEl(arr))


# using max method 
def largeEl(arr):
    large = arr[0]
    for i in range(len(arr)):
        large = max(large,arr[i])
    return large
arr = [55,32,97,99,3,67]
print(largestEl(arr))

def largestEl(arr):
    largest1 = 0
    for i in range(len(arr)):
        if arr[i] > largest1:
            largest1 = arr[i]
    return largest1
arr = [55,32,97,99,3,67]
print(largestEl(arr))
'''



def largest_ele(nums):
    n = len(nums)
    largets = 0
    for i in range(n):
        if nums[i] > largets:
            largets = nums[i]
    return largets
nums = [10,30,28]
print(largest_ele(nums))


def largest_ele_max(nums):
    n = len(nums)
    large = nums[0]
    for i in range(n):
        large = max(nums[0],nums[i])
    return large
nums = [10,30,28]
print(largest_ele(nums))


def largest_el(nums):
    n = len(nums)
    large = nums[0]

    for i in range(n):
        if nums[i] > large:
            large = nums[i]
    return large
nums = [10,20,50,1]
print(largest_el(nums))



def largest_element(nums):
    n = len(nums)
    largest_el = nums[0]

    for i in range(1,n):
        largest_el= max(largest_el,nums[i])
    return largest_el

nums = [10,20,10,39]
print(largest_element(nums))



def largest_ele(nums):
    n = len(nums)

    largest_ele = nums[0]
    for i in range(n):
        largest_ele = max(nums[i], largest_ele)
    return largest_ele
nums = [10,20,10,39,89]
print(largest_ele(nums))