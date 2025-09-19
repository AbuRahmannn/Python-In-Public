#given array consists of only 0,1 and 2
def arrayy(arr):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            cnt0 += 1
        elif arr[i] == 1:
            cnt1 += 1
        elif arr[i] == 2:
            cnt2 += 1
    i = 0            
    while (cnt0 > 0):
        arr[i] = 0
        i += 1
        cnt0 -= 1
    while (cnt1 > 0):
        arr[i] = 1
        i += 1
        cnt1 -= 1
    while (cnt2 > 0):
        arr[i] = 2
        i += 1
        cnt2 -= 1
    return arr        
arr = [0,2,1,2,0]
print(arrayy(arr))
