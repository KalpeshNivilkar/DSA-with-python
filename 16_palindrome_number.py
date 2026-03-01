
def isPalindrome(x):
        
        
    if x < 0:
        return False
        
    original = x
    reversed_num = 0
        
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x = x // 10
        
    return original == reversed_num
print(isPalindrome(121))



def palindrome(n):
    if n < 0:
        return False
    
    original = n
    rev_num = 0
    while n > 0:
        digit = n % 10
        rev_num = rev_num * 10 + digit
        n = n // 10
    return original == rev_num
print(palindrome(29))
