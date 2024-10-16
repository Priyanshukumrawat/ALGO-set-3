def max_in_subarrays(arr, N, K):
    result = []
    
   
    for i in range(N - K + 1):
        
        max_val = arr[i]
        for j in range(1, K):
            if arr[i + j] > max_val:
                max_val = arr[i + j]
        
  
        result.append(max_val)
    
    return result


arr1 = [1, 2, 3, 1, 4, 5]
K1 = 3
print(max_in_subarrays(arr1, len(arr1), K1))  

