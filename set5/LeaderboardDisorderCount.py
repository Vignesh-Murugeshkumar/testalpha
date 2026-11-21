def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, count_left = merge_sort(arr[:mid])
    right, count_right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    count = count_left + count_right

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1

        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, count
arr=[5,3, 8, 6, 2, 7]
print(merge_sort(arr)[1])