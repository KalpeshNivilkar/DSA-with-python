def majority_element(num):
    n = len(num)
    freq = 0
    ans = 0

    for i in num:
        if freq == 0:
            ans = i
        if i == ans:
            freq += 1
        else:
            freq -= 1
    return freq

arr = [1,2,2,2,2,2,2,3,1,1,1,2]
print("the majority element is :", majority_element(arr))
        