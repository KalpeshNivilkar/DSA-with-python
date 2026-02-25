def twoSum(num,target):
    for i in range(0,len(num)):
        for j in range(i+1,len(num)):
            if num[i] + num[j] == target:
                return [i,j]
            

arr = [2,7,11,15]
target = 9
print(twoSum(arr,target))