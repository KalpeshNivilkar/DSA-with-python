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
        



 