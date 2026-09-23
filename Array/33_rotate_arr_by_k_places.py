# brute approach 
def rotate_arr_by_k_places(nums,k):
    n = len(nums)
    rotations = k % n

    for _ in range(rotations):
        last = nums.pop()          #last element will pop out
        nums.insert(0, last)
    return nums
nums = [10,20,30,40]
print(rotate_arr_by_k_places(nums,1))


#better approach

def rotate(nums,k):
    n = len(nums)
    k = k % n

    nums[:] = nums[n-k:] + nums[:n - k]
    return nums
nums = [10,20,30,40]
print(rotate(nums,1))

# optimal solutions
class solution: 
    def reverse(self,nums,left,right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1

    def rotate(self,nums,k):
        n = len(nums)
        k  = k % n

        self.reverse(nums,n-k,n-1)  #reverse last eles
        self.reverse(nums,0,n-k-1)  #reverse first eles
        self.reverse(nums,0,n-1)    #reverse whole array

nums = [10,20,30,40]
print(rotate(nums,2))
