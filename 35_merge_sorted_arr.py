def merge_arr(num1,num2):
    result = []
    i = 0
    j = 0
    n = len(num1)
    m = len(num2)
    
    while i < n and j < m:
        if num1[i] <= num2[j]:
            result.append(num1[i])
            i += 1
        else:
            result.append(num2[j])
            j += 1
    
    while i < n:
        result.append(num1[i])
        i += 1
    
    while j < m:
        result.append(num2[j])
        j += 1

    return result

a = [1,3,5]
b = [2,4,6]

print(merge_arr(a,b))


