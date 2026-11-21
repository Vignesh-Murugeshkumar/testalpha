def product_popularity(arr):
    freq = {}
    # Calculate frequency
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    unique = list(freq.keys())
    def merge_sort(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = merge_sort(a[:mid])
        right = merge_sort(a[mid:])
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if freq[left[i]] < freq[right[j]]:
                merged.append(left[i])
                i += 1
            elif freq[left[i]] > freq[right[j]]:
                merged.append(right[j])
                j += 1
            elif left[i] > right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    ordered = merge_sort(unique)
    result = []
    for x in ordered:
        for _ in range(freq[x]):
            result.append(x)
    return result


arr=[4, 4, 6, 2, 2, 2, 6, 9, 6]

print(product_popularity(arr))