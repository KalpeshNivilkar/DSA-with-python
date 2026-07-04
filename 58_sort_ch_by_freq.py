# example
'''Input: s = "tree"
Output: "eetr"
Explanation: 'e' appears 2 times, 't' and 'r' appear once.
So "eetr" or "eert" are both valid answers.'''

def sort_char(s):
    result = ""
    hash_map = {}

    for ch in s:
        hash_map[ch] = hash_map.get(ch,0) + 1
    sorted_char = sorted(hash_map.items(),key= lambda x:x[1],reverse= True)
    for ch, freq in sorted_char:
        result += ch * freq
    return result
   
    
        

s = "tree"
print(sort_char(s))