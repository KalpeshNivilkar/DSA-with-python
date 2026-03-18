# brute-forse-approach
def productOfArray(arr):
    ans = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i != j:
                product *= arr[j]
        ans.append(product)
    return ans
arr = [1,2,3,4]
print(productOfArray(arr))

# optimized-approach
def productOfArray(arr):
    n = len(arr)
    ans = [1] * n
    left = 1
    for i in range(n):
        ans[i] = left
        left *= arr[i]
     
    right = 1
    for i in range(n-1,-1,-1):
        ans[i] = right
        right *= arr[i]
    return ans
arr = [1,2,3,4]
print(productOfArray(arr))
