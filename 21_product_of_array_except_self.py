def productOfArray(arr):
    ans = []

    for i in range(len(arr)):
        product = 1   # reset for each i

        for j in range(len(arr)):
            if i != j:
                product *= arr[j]   # use value

        ans.append(product)   # append after inner loop

    return ans

arr = [1, 2, 3, 4]
print(productOfArray(arr))