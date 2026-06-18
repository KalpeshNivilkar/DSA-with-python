def hash_table(nums):
    hash_map = {}

    for i in range(len(nums)):
        hash_map[nums[i]] = hash_map.get(nums[i],0) +1
    return hash_map
nums = [1,23,1,1,1,1,2,2,2,23,3,3,3]
print(hash_table(nums))