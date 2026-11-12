
def balancepoint(arr):
    total = 0

    # Calculate total sum
    for num in arr:
        total += num

    leftsum = 0

    for i in range(len(arr)):

        rightsum = total - leftsum - arr[i]

        if leftsum == rightsum:
            return i

        leftsum += arr[i]

    return -1


arr=[3, -2, 5, 4, 1, 5]

print(balancepoint(arr))
