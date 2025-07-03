# def dnfAlgorithm(number):
#     n = len(number)

#     low = 0
#     mid = 0
#     high = n - 1

#     while mid < high:
#         if number[mid] == 0:
#             number[low] , number[mid] = number[mid] , number[low]
#             low += 1
#             mid += 1
#         elif number[mid] == 1:
#             mid += 1
#         else:
#             number[high] , number[mid] = number[mid] ,number[high]
#             high -= 1
#     return number
# arr = [1,2,0,1,0,0,1,2,1,2,0]
# print(dnfAlgorithm(arr))

def dnfAlgo(el):
    n = len(el)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if el[mid] == 0:
            el[low] ,el[mid] = el[mid],el[low]
            low += 1
            mid += 1
        elif el[mid] == 1:
            mid += 1
        else:
            el[high],el[mid] = el[mid],el[high]
            high -= 1
        
    return el
arr = [1,2,0,1,0,0,1,2,1,2,0]
print(dnfAlgo(arr))