# there is a array which contain el like arr = [5,10,-3,-1,-10,6]
# output wiil be arr = [5,-3,10,-1,6,-10]


"""def rearrange_arr(arr):
    positive = []
    negative = []
    for num in arr:
        if num > 0:
            positive.append(num)
        else:
            negative.append(num)
    return result_arr(positive,negative)

def result_arr(positive,negative):
    result = []
    p = len(positive)
    n = len(negative)
    i = 0
    j = 0

    while i < p and j < n:
        result.append(positive[i])
        result.append(negative[j])
        i += 1
        j += 1

    while i < p:
        result.append(positive[i])
        i += 1

    while j < n:
        result.append(negative[j])
        j += 1
    
    return result

arr = [5, -3, 10, -1, 6, -10]
print(rearrange_arr(arr))"""




# optimal approach
def rearrange_arr(arr):
    n = len(arr)
    result =[0] * n
    posIndex = 0
    negIndex = 1
    for el in arr:
        if el >= 0:
            result[posIndex] = el
            posIndex += 2
        else:
            result[negIndex] = el
            negIndex += 2
    return result

arr = [5, -3, 10, -1, 6, -10]
print(rearrange_arr(arr))
  

   
    
