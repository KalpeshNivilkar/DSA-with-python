def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)  
        quicksort(arr, pivot_index + 1, high)  

def partition(arr, low, high):
    pivot = arr[low]  
    i = high + 1

    for j in range(high, low, -1):
        if arr[j] >= pivot:
            i -= 1
            arr[i], arr[j] = arr[j], arr[i]  

    arr[i - 1], arr[low] = arr[low], arr[i - 1]  
    return i - 1


arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr) - 1)
print( arr)  