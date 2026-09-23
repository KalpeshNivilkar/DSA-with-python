def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]       
        j = i - 1           

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   
            j -= 1

        arr[j + 1] = key   

    return arr

arr = [5, 3, 4, 1]
print(insertion_sort(arr))




def Insertion_sort(nums):
    n = len(nums)

    for i in range(1,n):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums
nums = [5, 3, 4, 1]
print(Insertion_sort(nums))


def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key
    return nums
nums = [5,3,4,1]
print(insertion_sort(nums))



def insertion_sort3(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]     #1 idx
        j = i - 1         #0 idx

        while j >= 0 and nums[j] > key:             #nums[0idx] > nums[1idx]
            nums[j+1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
nums = [10,30,23,11]
print(insertion_sort3(nums))






def insertion_sort4(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i -1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j +1] = key
    return arr
nums = [10,30,23,11]
print(insertion_sort4(nums))


def insertion_sort(nums): 
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i -1

        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key
    return nums

nums = [10,30,23,11,22]
print(insertion_sort(nums))

'''Here's the dry run for insertion_sort([10, 30, 23, 11, 22]):

i = 1, key = nums[1] = 30, j = 0

nums[0]=10 > 30? No → loop doesn't run
nums[1] = key → [10, 30, 23, 11, 22] (no change)

i = 2, key = nums[2] = 23, j = 1

nums[1]=30 > 23? Yes → nums[2] = nums[1] → [10, 30, 30, 11, 22], j = 0
nums[0]=10 > 23? No → stop
nums[1] = key(23) → [10, 23, 30, 11, 22]

i = 3, key = nums[3] = 11, j = 2

nums[2]=30 > 11? Yes → nums[3] = nums[2] → [10, 23, 30, 30, 22], j = 1
nums[1]=23 > 11? Yes → nums[2] = nums[1] → [10, 23, 23, 30, 22], j = 0
nums[0]=10 > 11? No → stop
nums[1] = key(11) → [10, 11, 23, 30, 22]

i = 4, key = nums[4] = 22, j = 3

nums[3]=30 > 22? Yes → nums[4] = nums[3] → [10, 11, 23, 30, 30], j = 2
nums[2]=23 > 22? Yes → nums[3] = nums[2] → [10, 11, 23, 23, 30], j = 1
nums[1]=11 > 22? No → stop
nums[2] = key(22) → [10, 11, 22, 23, 30]

Final output: [10, 11, 22, 23, 30]'''

def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key
    return nums

nums = [10,2090,80,70]
print(insertion_sort(nums))