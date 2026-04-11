# def remove_duplicate(arr):
#     n = len(arr)
#     freq_dic = {}
#     for i in range(0,n):
#         freq_dic[arr[i]] = 0
   
#     j = 0
#     for k in freq_dic:
#         arr[j] = k
#         j += 1
#     return j



def remove_duplicates(arr):
    n = len(arr)
    if n == 1:
        return 1
    i = 0
    j = i + 1
    while j < n:
        if arr[i] != arr[j]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
        j += 1
    return i
   
arr = [10,50,30,10,20,]
print(remove_duplicates(arr))







