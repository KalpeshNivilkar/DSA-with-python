def longestConsecutive(nums):
    num_set = set(nums)

    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num 
            count = 1

            while current + 1 in num_set:
                current += 1
                count += 1
            
            longest = max(longest,count)
    return longest
arr = [1,99,101,98,2,5,3,100]
print(longestConsecutive(arr))

print("brute-force-code")

def longest_consecutive(nums):
    n = len(nums)
    max_count = 0

    for i in range(n):
        num = nums[i]
        count = 1
        while num + 1 in nums:
            count += 1
            num = num + 1
        max_count = max(count,max_count)
    return max_count
    
nums = [1,99,101,98,2,5,3,100]
print(longest_consecutive(nums))

print("better solution")

def long_consecutive(nums):
    nums.sort()
    n = len(nums)
    smallest_num = float('-inf')
    count = 0
    longest = 0

    for i in range(n):
        num = nums[i]
        if num -1 == smallest_num:
            count += 1
            smallest_num = num

        elif num -1 != smallest_num:
            count = 1
            smallest_num = num
        longest = max(count, longest)
    return longest
nums = [1,99,101,98,2,5,3,100]
print(long_consecutive(nums))


print("optimal approach")
def long_cons(nums):
    n = len(nums)
    my_set = set()

    for i in range(n):
        my_set.add(nums[i])

    longest = 0
    for num in my_set:
        if num -1 not in my_set:
            current = num
            count = 1

            while current + 1 in my_set:
                count += 1
                current = current + 1
            longest = max(longest, count)
    return longest
nums = [1,99,101,98,2,5,3,100]
print(long_cons(nums))