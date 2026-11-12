
def reverse(arr, left, right):

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1


def rotate(arr, k):

    n = len(arr)

    k = k % n

    # Reverse entire array
    reverse(arr, 0, n - 1)

    # Reverse first k elements
    reverse(arr, 0, k - 1)

    # Reverse remaining elements
    reverse(arr, k, n - 1)

    return arr


n, k = 7,3

arr =[5, 3, 8, 2, 7, 1, 9]

rotate(arr, k)

print(*arr)
