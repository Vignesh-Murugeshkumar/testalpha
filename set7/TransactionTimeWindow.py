def firstindex(arr,target):
    n=len(arr)
    high=n-1
    low=0
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            answer=mid
            high=mid-1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return answer
def lastindex(arr,target):
    n=len(arr)
    high=n-1
    low=0
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            answer=mid
            low=mid+1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return answer
arr=[5, 7, 7, 8, 8, 8, 8, 10, 12, 12]
print(firstindex(arr,8))
print(lastindex(arr,8))