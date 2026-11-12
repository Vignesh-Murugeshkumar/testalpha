
def fastestDeliveries(arr, k):

    n = len(arr)

    for i in range(k):

        min_index = i

        # Find the smallest element
        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap smallest element with current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr[:k]


# Input
arr = [29, 14, 36, 7, 21, 14, 50]
k = 3

# Output
print(fastestDeliveries(arr, k))
