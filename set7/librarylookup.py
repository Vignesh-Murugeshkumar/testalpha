def librarlookup(arr,target):
    n=len(arr)
    high=n-1
    low=0
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[10, 20, 30, 40, 50, 60]    
print(librarlookup(arr,30))