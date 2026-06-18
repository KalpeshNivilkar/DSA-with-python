# store frequency

def store_freq(nums):
    n = len(nums)
    freq_map = {}

    for i in range(n):
        if nums[i] in freq_map:
            freq_map[nums[i]] += 1
        else:
            freq_map[nums[i]] = 1
    return freq_map

nums = [1,2,3,1,1,1,1,2,2,3,3]
print(store_freq(nums))


# method 2
def store_freq_2(nums):
    hash_map = {}
    n = len(nums)

    for i in range(n):
        hash_map[nums[i]] = hash_map.get(nums[i],0)+ 1
    return hash_map
nums = [1,2,3,1,1,1,1,2,2,3,3]
print(store_freq(nums))



# store frequency in dictionary
def store_freq(nums):
    freq_dict = {}
    for i in range(len(nums)):
        if nums[i] in freq_dict:
            freq_dict[nums[i]] += 1
        else:
            freq_dict[nums[i]] = 1
    return freq_dict

nums = [1,2,3,1,1,1,1,2,2,1,1]
print(store_freq(nums))


# method no 2

def sec_method(nums):
    n = len(nums)
    freq_map = {}
    for i in range(n):
        freq_map[nums[i]] = freq_map.get(nums[i],0) +1
    return freq_map
nums = [1,2,3,1,1,1,1,2,2,1,1]
print(sec_method(nums))


     
