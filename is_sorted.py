def is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i] > arr[i + 1]:
            return False
    return True
                
           
  
arr = [55,32,97,99,3,67]
print(is_sorted(arr))