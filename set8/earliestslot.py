def ealiestslot(arr):
    low=0
    high=len(arr)-1
    while low<high:
        mid=low+(high-low)//2
        if arr[mid]>arr[high]:
            low=mid+1
        else:
            high=mid
    return arr[low]
arr=[40,50,60,70,10,20,30]
print(ealiestslot(arr))