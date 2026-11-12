
def insertionSort(arr):
    n = len(arr)
    shifts = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        arr[j + 1] = key
    return arr, shifts
arr = [10, 20, 15, 30, 40, 35, 50, 45]
print(insertionSort(arr))
