def sum(A, N):
    if N == 1:
        return A[0]
    
    if A[0] > A[1]:
        maxi = A[0]
        mini = A[1]
    else:
        maxi = A[1]
        mini = A[0]
    
    for i in range(2, N):
        if A[i] > maxi:
            maxi = A[i]
        elif A[i] < mini:
            mini = A[i]
    
    return maxi + mini


# Example usage
A = [12, 45, 23, 78, 23]
N = len(A)

print(sum(A, N))  # Output: 90 (78 + 12)
