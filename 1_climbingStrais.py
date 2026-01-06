# def climbStrairs(n):
#     memo = {}
#     def fun(n):
#         if(n < 2):
#             return 1
#         if n in memo:
#              return memo[n]
#         memo[n] = fun(n-1) + fun(n-2)
#         return memo[n]
#     return fun(n)

# print(climbStrairs(5))
    
"""""def climbStrairs(n):
    memo = {}
    def fun(n):
        if(n < 2):
            return 1
        if n in memo:
            return memo[n]
        memo[n] = fun(n-1) + fun(n-2)
        return memo[n]

        
    return fun(n)
print(climbStrairs(20))"""""



"""""def climbingStrairs(n):
    memo = {}
    def fun(n):
        if n < 2:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = fun(n-1) + fun(n-2)
        return memo[n]
    
    return fun(n)
print(climbingStrairs(30))"""""


def climbingStrairs(n):
    memo = {}
    def fun(n):
        if n < 2:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = fun(n-1) + fun(n-2)
        return memo[n]
    
    return fun(n)
print(climbingStrairs(30))

        
             