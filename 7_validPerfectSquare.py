def validSquare(num):
    # if num == 0:
    #     return False
    for i in range (0,int(num **0.5)+1):
        if i * i == num:
            return True
    return False    
print(validSquare(16))