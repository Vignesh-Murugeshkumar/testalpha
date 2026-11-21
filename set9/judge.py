
def trimmed_mean(arr, n, t):
    freq = [0] * 101

    for score in arr:
        freq[score] += 1
    total = 0
    count = 0
    skip_low = t
    remaining = n - 2 * t
    for score in range(101):
        occurrences = freq[score]
        if occurrences == 0:
            continue
        if skip_low > 0:
            removed = min(occurrences, skip_low)
            occurrences -= removed
            skip_low -= removed
        take = min(occurrences, remaining - count)
        total += score * take
        count += take
        if count == remaining:
            break
    return total / remaining
arr=[8, 9, 7, 10, 6, 9, 5, 8, 9, 10]
t = 2
n = len(arr)
result = trimmed_mean(arr, n, t)
print("%.2f" % result)
