''''def remove_paranthesis(s):
    count = 0
    result = ""
    for ch in s:
        if ch == "(":
            if count > 0:
                result += ch
            count += 1
        
        else:
            count -= 1
            if count > 0:
                result += ch
    return result

s = "(())(())"
print(remove_paranthesis(s))

        
def removeOuterParentheses(s):
    result = ""
    count = 0
    for ch in s:
        if ch == "(":
            count += 1
            if count > 1:
                result += ch
        else:
            count -= 1
            if count > 0:
                result += ch
    return result
s = "(())(())"
print(removeOuterParentheses(s))


def remove_parantheses(s):
    count = 0
    result = ""
    for ch in s:
        if ch == "(":
            count += 1
            if count > 1:
                result += ch
        else:
            count -= 1
            if count > 0:
                result += ch
    return result
s = "(())(())"
print(remove_parantheses(s))



def dictionary(nums):
    hash_map = {}
    for i in range(len(nums)):
        if nums[i] in hash_map:
            hash_map[nums[i]] += 1
        else:
            hash_map[nums[i]] = 1
    return hash_map



def store_freq(nums):
    hash_table = {}
    for i in range(len(nums)):
        hash_table[nums[i]] = hash_table.get(nums[i],0) + 1
    return hash_table'''



'''def remove_parantheses(s):
    count = 0
    result = ""

    for ch in s:
        if ch == "(":
            count += 1
            if count > 1:
                result += ch
        else:
            count -= 1
            if count > 0:
                result += ch
    return result
s = "(())(())"
print(remove_parantheses(s))




def remove_parantheses(s):
    count = 0
    result = ""
    for ch in s:
        if ch == "(":
            count += 1
            if count > 1:
                result += ch
        else:
            count -= 1
            if count > 0:
                result += ch
    return result
s = "((()))(())"
print(remove_parantheses(s))'''

def remove_parantheses(s):
    result = ""
    count = 0
    for ch in s:
        if ch == "(":
            count += 1
            if count > 1:
                result += ch
        else:
            count -= 1
            if count > 0:
                result += ch
    return result
s = "((()))(())"
print(remove_parantheses(s))