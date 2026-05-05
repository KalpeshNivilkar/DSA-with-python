# brute force approach 
def fourSum(target,arr):
    n = len(arr)
    my_set = set()

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    total = arr[i]+arr[j]+arr[k]+arr[l]
                    if total == target:
                        temp = [arr[i],arr[j],arr[k],arr[l]]
                        temp.sort()
                        my_set.add(tuple(temp))
    
    return [list(ans) for ans in my_set]

arr = [1,0,-1,0,-2,2]
target = 0

print(fourSum(target,arr))


# better approach

def fourSum(arr,target):
    n = len(arr)
    myset = set()

    for i in range(n): 
        for j in range(i + 1,n):
            hashset = set()
            for k in range(j+1,n):
                fourth = target - (arr[i]+arr[j]+arr[k])

                if fourth in hashset:
                    temp = [arr[i],arr[j],arr[k],fourth]
                    temp.sort()
                    myset.add(tuple(temp))
                hashset.add(arr[k])

    return [list(ans) for ans in myset]

arr = [1,0,-1,0,-2,2]
target = 0

print(fourSum(arr,target))


# optimal approach
def foursum(arr,target):
    n = len(arr)
    ans =[]
    arr.sort()

    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        for j in range(i+1,n):
            if j > i+1 and arr[j] == arr[j-1]:
                continue

            k = j+1
            l = n-1

            while k < l:
                total = arr[i] + arr[j] +arr[k] +arr[l]
                if total == target:
                    ans.append([arr[i],arr[j],arr[k],arr[l]])
                    k += 1
                    l -= 1

                    while k < l and arr[k] == arr[k-1]:
                        k += 1
                    
                    while l > k and arr[l] == arr[l+1]:
                        l -= 1
                
                elif total < target:
                    k += 1
                else:
                    l -= 1

arr = [1,0,-1,0,-2,2]
target = 0

print(fourSum(arr,target))


      

    
