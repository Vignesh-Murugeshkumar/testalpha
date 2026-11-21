def sensorreading(arr):
    n=len(arr)
    high=n-1
    low=0
    mid=0
    while mid<=high:
        if arr[mid]==1:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==2:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr
arr=[3, 1, 3, 2, 3, 1, 2, 3, 1, 3]
print(sensorreading(arr))