"""# using sort 
def secLargeEl(arr):
    n = len(arr)
    arr.sort()
    return arr[n-2]
arr = [55,32,97,99,3,67]
print(secLargeEl(arr))"""


def secLarEl(arr):
    n = len(arr)
    largest = arr[0]
    secLargest = arr[0]
    for i in range(len(arr)):
        largest = max(largest,arr[i])
  
    for j in range(len(arr)):
        if arr[j] != largest and arr[j] > secLargest:
            secLargest = arr[j]
    return secLargest
       
    
arr = [55,32,97,99,3,67]
print(secLarEl(arr))
        


def secLarge(arr):
    largest = arr[0]
    s_large = arr[0]   # second largest initial

    # Find largest
    for i in range(len(arr)):
        largest = max(largest, arr[i])

    # Find second largest
    for i in range(len(arr)):
        if arr[i] != largest and arr[i] > s_large:
            s_large = arr[i]

    return s_large
arr = [55,32,97,99,3,67]
print(secLarEl(arr))



def second_large(nums):
    n = len(nums)

    largest = nums[0]
    second_large = nums[0]

    for i in range(n):
        largest = max(largest,nums[i])

    for i in range(n):
        if nums[i] != largest and nums[i] > second_large:
            second_large = nums[i]

    return second_large
arr = [55,32,97,99,3,67]
print(secLarEl(arr))