def studentidinsertionpoint(arr,id):
    n=len(arr)
    high=n-1
    low=0
    while low<high:
        mid=low+(high-low)//2
        if arr[mid]<id:
            low=mid+1
        else:
            high=mid
    return low
arr=[10, 20, 30, 45, 60, 80]
id=50
print(studentidinsertionpoint(arr,id))