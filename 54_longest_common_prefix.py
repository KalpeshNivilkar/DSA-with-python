'''Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"'''
'''def longest_common_prefix(strs):
    if strs == "":
        return ""
    result = ""
    base = strs[0]
    for i in range(len(base)):
        for word in strs[1:]:
            if  word[i] != base[i]:
                return result
        result += base[i]
    return result
strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))'''




def long_common_prefix(strs):
    if not strs == "":
        return ""
    result = ""
    base = strs[0]

    for i in range(len(base)):
        for word in strs[1:]:
            if word[i] != base[i]:
                return result
        result += base[i]
    return result
strs = ["flower","flow","flight"]
print(long_common_prefix(strs))
       

