"""def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [11,34,21,10,55]
print(selection_sort(arr))





def selection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i],arr[min_index] = arr[min_index],arr[i]

    return arr 

arr = [50,23,11,12,44]
print(selection(arr))

        

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index],arr[i]
    return arr

arr = [10,23,12,43,55,22]
print(selection_sort(arr))

def selction_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
arr = [10,23,12,43,55,22]
print(selection_sort(arr))"""


def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i],nums[min_index] = nums[min_index], nums[i]
    return nums




nums = [10,15,50,30,20]
print(selection_sort(nums))


def selection(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j],nums[i]
    return nums
nums = [10,15,50,30,20]
print(selection(nums))



def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums
nums = [10,20,9,11]
print(selection_sort(nums))