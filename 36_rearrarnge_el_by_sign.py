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
  

   
# brute force approach
  
def rearrage_num_by_sign(nums):
    sort_num = sorted(nums)
    n = len(sort_num)
    pos_el = []
    neg_el = []

    for i in range(n):
        if sort_num[i] > 0:
            pos_el.append(sort_num[i])
        else:
            neg_el.append(sort_num[i])

    return arrange_num(pos_el, neg_el)

def arrange_num(pos_el,neg_el):
    final_list = []
    i = 0
    j = 0
    p = len(pos_el)
    n = len(neg_el)

    while i < p and j < n:
        final_list.append(pos_el[i])
        i += 1
        final_list.append(neg_el[j])
        j += 1

    return final_list
        
nums = [-2, 3, 4, -1]
print(rearrage_num_by_sign(nums))

# optimal approach
print("this is optimal solution...")

def rearrange_num(nums):
    n = len(nums)
    result = [0] * n
    pos_idx = 0
    neg_idx = 1

    for el in nums:
        if el >= 0:
            result[pos_idx] = el
            pos_idx += 2
        else:
            result[neg_idx] = el
            neg_idx += 2
        
    return result

nums = [-2, 3, 4, -1]
print(rearrange_num(nums))