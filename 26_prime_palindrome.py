def prime_number(self, num):
    if num < 2:                              # ✅ fix 1
        return False
    for i in range(2, int(num ** 0.5) + 1): # ✅ fix 2
        if num % i == 0:
            return False
    return True

def palindrome_number(self, num):
    rev = 0
    og_num = num
    if num <= 1:
        return False
    while num > 0:                           # ✅ fix 3
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    if rev == og_num:
        return True

def is_prime_and_palidrome(self, num):
    while True:
        if self.prime_number(num) and self.palindrome_number(num):
            return num
        num += 1

class Solution:
    prime_number = prime_number
    palindrome_number = palindrome_number
    is_prime_and_palidrome = is_prime_and_palidrome

num = 6
obj = Solution()                             
print(obj.is_prime_and_palidrome(num))       