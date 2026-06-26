'''def reverse_word_in_string(s):
    split_s = s.split()
    n = len(split_s)
    left = 0
    right = n - 1
    while left > right:
        split_s[left] , split_s[right] = split_s[right],split_s[left]
        left += 1
        right -= 1
    return split_s'''








'''s = "the sky is blue"
split_S = s.split()
print(split_S)     # ['the', 'sky', 'is', 'blue']
n = len(split_S)
left = 0
right = n - 1

while left <= right:
    split_S[left], split_S[right] = split_S[right],split_S[left]
    left += 1
    right -= 1
print(split_S)'''


def rev_words(s):
    new_s = s.split()
    n = len(new_s)
    l = 0
    r = n - 1

    while l <= r:
        new_s[l], new_s[r] = new_s[r], new_s[l]
        l += 1
        r -= 1
    return(" ".join(new_s))
s = "the sky is blue"
print(rev_words(s))



# reverse word in a string 
def rev_word(s):
    new_s = s.split()
    n = len(new_s)
    left = 0
    right = n-1

    while left <= right:
        new_s[left],new_s[right] = new_s[right], new_s[left]
        left += 1
        right -= 1
    return(" ".join(new_s))
s = "the sky is blue"
print(rev_word(s))



def rev_words(s):
    s_new = s.split()
    n = len(s_new)
    left = 0
    right = n - 1

    while left <= right:
        s_new[left], s_new[right] = s_new[right], s_new[left]
        left += 1
        right -= 1
    return (" ".join(s_new))
s = "the sky is blue"
print(rev_words(s))