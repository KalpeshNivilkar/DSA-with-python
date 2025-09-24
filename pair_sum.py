def pair_sum(arr, target):

    pairs = []
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    
    return pairs

arr = [2, 4, 3, 5, 7, 8, 9]
target = 10

print(pair_sum(arr,target))