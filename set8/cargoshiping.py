def cargo_shipping(weights, D):

    low = weights[0]
    high = 0
    for w in weights:
        if w > low:
            low = w
        high += w
    while low < high:
        mid = low + (high - low) // 2
        days = 1
        current_weight = 0
        for w in weights:
            if current_weight + w <= mid:
                current_weight += w
            else:
                days += 1
                current_weight = w
        if days <= D:
            high = mid
        else:
            low = mid + 1
    return low



arr=[4, 2, 7, 1, 8, 3, 5]
d=3

print(cargo_shipping(arr, d))