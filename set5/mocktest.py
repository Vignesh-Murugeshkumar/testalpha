
def bubbleSort(arr):

    n = len(arr)
    passes = 0

    for i in range(n - 1):

        swapped = False

        for j in range(n - 1 - i):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        if swapped:
            passes += 1
        else:
            break

    return arr, passes


arr = [5, 1, 4, 2, 8]

result, passes = bubbleSort(arr)

print(*result)
print(passes)
