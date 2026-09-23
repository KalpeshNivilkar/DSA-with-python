def two_sum(num):
    n = len(num)
    for i in range(n):
        for j in range(i + 1, n):
            if num[i] + num[j] == target:
                return [i,j]
            

arr = [2,4,6,9,10]
target = 10
print("two index of target values are:", two_sum(arr))

        