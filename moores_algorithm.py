def majorityElement(num):
    n = len(num)
    for i in num:
        freq = 0
        for j in num:
            if i == j:
                freq += 1
        
        if freq >= n //2:
            return i
        

arr = [1,2,3,1,1,1,2]
print(majorityElement(arr))