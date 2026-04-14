def rorate_arr(arr):
    k = 3
    for _ in range(0,k):
        e = arr.pop()
        arr.insert(0,e)
    return arr
arr = [10,23,44,22]
print(rorate_arr(arr))