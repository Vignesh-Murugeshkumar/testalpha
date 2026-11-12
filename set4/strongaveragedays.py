
def strongaverage(arr, k, T):

    window = 0
    count = 0

    for i in range(k):
        window += arr[i]

    if window >= k * T:
        count += 1

    for i in range(k, len(arr)):

        window = window - arr[i-k] + arr[i]

        if window >= k * T:
            count += 1

    return count


arr=[2,2,2,2,5,5,8]
k=3
T=4

print(strongaverage(arr, k, T))
