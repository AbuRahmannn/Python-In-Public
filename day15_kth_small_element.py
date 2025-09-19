def ksmall(arr,k):
    n = len(arr)
    if n == 1:
        return arr[0]
    arr.sort()
    return arr[k-1]

    

arr = [23,56,34,87,45]   
print(arr)
k = int(input("element to be find Kth smallest element"))
print(ksmall(arr,k))
