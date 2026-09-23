def rev_arr(arr,left,right):
   
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr

nums = [1,2,34,1,2,3,41,3]
print(rev_arr(nums,3,6))

