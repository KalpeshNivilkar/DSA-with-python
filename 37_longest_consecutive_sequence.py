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