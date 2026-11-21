def budgetpairing(arr, target):
    st = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in st:
            return st[complement], i
        st[arr[i]] = i
    return -1
arr = [3, 8, 12, 19, 25, 31, 40]
target = 44
print(budgetpairing(arr, target))