def dnfAlgorithm(number):
    n = len(number)

    low = 0
    mid = 0
    high = n - 1

    while mid < high:
        if number[mid] == 0:
            number[low] , number[mid] = number[mid] , number[low]
            low += 1
            mid += 1
        elif number[mid] == 1:
            mid += 1
        else:
            number[high] , number[mid] = number[mid] ,number[high]
            high -= 1
    return number
arr = [1,2,0,1,0,0,1,2,1,2,0]
print(dnfAlgorithm(arr))

