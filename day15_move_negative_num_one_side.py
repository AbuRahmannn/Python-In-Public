def neg(arr):
    j = 0
    n = len(arr)
    for i in range(0,n):
        if(arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j+1
    return arr
arr = [3,-4,67,-1,9]
print(neg(arr))
