
def peaktraffic(arr, k):

    window = 0

    # Calculate first window sum
    for i in range(k):
        window += arr[i]

    largest = window

    # Slide the window
    for i in range(k, len(arr)):

        window = window - arr[i-k] + arr[i]

        if window > largest:
            largest = window

    return largest



arr = [4,2,10, 1, 3, 9, 6, 5, 7]
k=3
print(peaktraffic(arr, k))
