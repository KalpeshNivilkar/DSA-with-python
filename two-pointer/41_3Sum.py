# bruteforce approach 

def three_sum(arr):
    my_set = set()
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == 0:
                    temp = [arr[i],arr[j],arr[k]]
                    temp.sort()
                    my_set.add(tuple(temp))
    
    return [list(ans)for ans in my_set]

arr = [1,2,1,2,1,-1,-2,-1,0,0,0,1]
print(three_sum(arr))

# better approach

def threeSum(arr):
    result = set()
    n = len(arr)
    for i in range(0,n):
        my_set =  set()
        for j in range(i+1,n):
            third = -(arr[i]+arr[j])
            if third in my_set:
                temp = [arr[i],arr[j],third]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(arr[j])
        
    return [list(ans) for ans in result]

arr = [1,2,1,2,1,-1,-2,-1,0,0,0,1]
print(threeSum(arr))
                
# brute force approach

print("this is brute force solution")
def three_sum(nums):
    n = len(nums)
    my_set = set()

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+ nums[j]+ nums[k] == 0:
                    temp = [nums[i],nums[j],nums[k]]
                    temp.sort()
                    my_set.add(tuple(temp))
    return[list(ans) for ans in my_set]
nums = [1,2,1,2,1,-1,-2,-1,0,0,0,1]
print(three_sum(nums))

# brute force approach

print("this is brute force solution")
def three_sum(nums):
    n = len(nums)
    my_Set = set()

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+ nums[j]+ nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    my_Set.add(tuple(temp))

    return [list(ans) for ans in my_Set]
nums = [1,2,1,2,1,-1,-2,-1,0,0,0,1]
print(three_sum(nums))


    