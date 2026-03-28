"""def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr    
arr = [10,23,12,43,55,22]
print(bubble_sort(arr))"""



def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
arr = [12,44,22,11,55]
print(selection_sort(arr))