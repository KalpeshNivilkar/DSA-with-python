# def remove_duplicate(arr):
#     n = len(arr)
#     freq_dic = {}
#     for i in range(0,n):
#         freq_dic[arr[i]] = 0
   
#     j = 0
#     for k in freq_dic:
#         arr[j] = k
#         j += 1
#     return j



def remove_duplicates(arr):
    n = len(arr)
    if n == 1:
        return 1
    i = 0
    j = i + 1
    while j < n:
        if arr[i] != arr[j]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
        j += 1
    return i
   
arr = [10,50,30,10,20,]
print(remove_duplicates(arr))










def remove_duplicate(nums):
    # n = len(nums)
    new_list = set(nums)
    return list(new_list)
    

nums = [10,20,30,40,40]
print(remove_duplicate(nums))

def remove_duplicates(nums):
    n = len(nums)
    i = 0

    for j in range(1, n):
        if nums[i] != nums[j]:
            i+= 1
            nums[i] = nums[j]
    return nums[i+ 1]
nums = [10,20,30,40,40]
print(remove_duplicates(nums))



# def remove_duplicate(nums):
#     n = len(nums)
#     i = 0

#     for j in range(1,n):
#         if nums[i] != nums[j]:
#             i+= 1
#             nums[i] = nums[j]
#     return i + 1






def remove_duplicates(nums):
   
   result = set(nums)
   return list(result)

            
    
nums = [1,1,1,3,4,5,6]
print(remove_duplicates(nums))

# leetcode ans 

def remove_diplicates(nums):
    n = len(nums)
    if n <= nums:
        return nums

    i = 0
    j = i +1

    while j < n:
        if nums[i] != nums[j]:
            i += 1
            nums[i],nums[j+1] = nums[j+1],nums[i]
        j += 1
    return nums
nums = [1,1,1,3,4,5,6]
print(remove_duplicates(nums))