def seatchartlook(arr, target):
    R = len(arr)
    C = len(arr[0])
    low = 0
    high = R * C - 1
    while low <= high:
        mid = low + (high - low) // 2
        row = mid // C
        col = mid % C
        if arr[row][col] == target:
            return row, col
        elif arr[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, -1
arr = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
print(seatchartlook(arr, 16))