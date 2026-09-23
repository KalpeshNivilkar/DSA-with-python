# brute-force-approach 
'''def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    sort_s = sorted(s)
    sort_t = sorted(t)
    if sort_s == sort_t:
        return True
    return False

s = "zonjlobp"
t = "lobpzonj"

print(valid_anagram(s,t))
'''

# optimal approach 
def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    
    store_dict = {}
    for ch in s:
        store_dict[ch] = store_dict.get(ch, 0) + 1
    for ch in t:
        if ch not in store_dict:
            return False
        else:
            if store_dict[ch] == 0:
                return False
            else:
                store_dict[ch] -= 1
    return True
s = "zonjlobp"
t = "lobpzonj"

print(valid_anagram(s,t))


def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    store_dict = {}
    for ch in s:
        store_dict[ch] = store_dict.get(ch,0) + 1
    for ch in t:
        if ch not in store_dict:
            return False
        else:
            if store_dict[ch] == 0:
                return False
            else:
                store_dict[ch] -= 1
        return True
s = "zonjlobp"
t = "lobpzonj"

print(valid_anagram(s,t))

    

