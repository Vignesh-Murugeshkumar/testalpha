def firstfailingnightlybuild(arr):
    n=len(arr)
    high=n-1
    low=0
    while low<high:
        mid=low+(high-low)//2
        if arr[mid]==0:
            low=mid+1
        else:
            high=mid
    return low
arr=[0, 0, 0,0, 0,0, 0, 1, 1, 1, 1, 1]
print(firstfailingnightlybuild(arr))