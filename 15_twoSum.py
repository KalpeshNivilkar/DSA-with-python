'''def twoSum(num,target):
    for i in range(0,len(num)):
        for j in range(i+1,len(num)):
            if num[i] + num[j] == target:
                return [i,j]
            

arr = [2,7,11,15]
target = 9
print(twoSum(arr,target))'''

def two_sum(num ,target):
    d = dict()
    for i in range(len(num)):
        d[num[i]] = i
    for i in range(len(num)):
        need = target - num[i]
        if(need in d.keys() and d[need] != i):
            return[i,d[need]]

num = [2,7,11,15]
target = 9
print(two_sum(num,target))

# brute_force_approach
def two_sum(nums,target):
    n = len(nums)

    for i in range(n):
        for j in range(1,n):
            if nums[i] + nums[j] == target:
                return [i,j]

num = [2,7,11,15]
target = 9
print(two_sum(num,target))

# optimal_appatoach
def two_sum_2(nums,target):
    n = len(nums)
    hash_map = {}
    for i in range(n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[nums[i]] = i
    return []
num = [2,7,11,15]
target = 9
print(two_sum_2(num,target))