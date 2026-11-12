
def longestUniqueScanRun(arr):

    last = {}
    left = 0
    best = 0

    for i in range(len(arr)):

        num = arr[i]

        # Check duplicate inside current window
        if num in last and last[num] >= left:
            left = last[num] + 1

        # Update last occurrence
        last[num] = i

        # Calculate current window length
        current = i - left + 1

        if current > best:
            best = current

    return best



arr = [12, 7, 9, 4, 5, 3, 12, 6, 8, 2]

print(longestUniqueScanRun(arr))
