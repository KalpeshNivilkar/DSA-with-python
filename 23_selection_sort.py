def selection_sort(arr):
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