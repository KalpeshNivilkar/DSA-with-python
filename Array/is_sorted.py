'''def is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i] > arr[i + 1]:
            return False
    return True
                
           
  
arr = [55,32,97,99,3,67]
print(is_sorted(arr))
'''



def check_array_is_sorted(nums):
    n = len(nums)
    for i in range(1, n):
        if nums[i] > nums[i+1]:
            return False
        return True

nums = [10,2030,20]
print(check_array_is_sorted(nums))