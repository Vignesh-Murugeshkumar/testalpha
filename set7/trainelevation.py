def find_peak(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low


def binary_search(arr, target, low, high, descending=False):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        if not descending:
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if arr[mid] > target:
                low = mid + 1
            else:
                high = mid - 1
    return -1
def trail_elevation_search(arr, h):
    peak = find_peak(arr)
    result = binary_search(arr, h, 0, peak)
    if result != -1:
        return result
    return binary_search(arr, h, peak + 1, len(arr) - 1, True)
arr=[2, 5, 9, 14, 20, 17, 11, 6, 1]
h = 11
print(trail_elevation_search(arr, h))