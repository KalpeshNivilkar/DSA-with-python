def majorityElement(num):
    n = len(num)
    freq = 0
    ans = 0

    for i in num:
        if freq == 0:
            ans = i
        # Count matching vs non-matching elements
        if i == ans:
            freq += 1
        else:
            freq -= 1

    return ans  # Moved outside the loop

   

arr = [1,2,2,2,2,2,2,3,1,1,1,2]
print(majorityElement(arr))