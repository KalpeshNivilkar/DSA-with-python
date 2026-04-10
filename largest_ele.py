"""def largestEl(arr):
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
