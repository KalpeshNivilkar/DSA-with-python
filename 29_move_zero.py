def moveZero(arr):
    j = 0
    for i in range(len(arr)):
        if i != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
    return arr
arr = [0,1,0,2,15]
moveZero(arr)