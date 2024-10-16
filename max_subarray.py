def find_subarray_or(A, N):
    resultOR = 0
    currOR = 0

    for i in range(N):
   
        currOR |= A[i]
        resultOR |= currOR
    
    return resultOR

A1 = [1, 4, 6]
N1 = len(A1)
print(find_subarray_or(A1, N1))  

