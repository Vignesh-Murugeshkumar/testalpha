
def findFloorCeil(arr,  q):
    n=len(arr)
    left = 0
    right = n - 1
    floor = None
    ceil = None
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == q:
            return arr[mid], arr[mid]
        elif arr[mid] < q:
            floor = arr[mid]
            left = mid + 1
        else:
            ceil = arr[mid]
            right = mid - 1
    return floor, ceil
arr=[10, 20, 30, 40, 50, 60]
q=35
print(findFloorCeil(arr, q))


