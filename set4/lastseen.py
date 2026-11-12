
def repeatedlogin(arr, k):

    lastseen = {}

    for i in range(len(arr)):

        if arr[i] in lastseen:

            if i - lastseen[arr[i]] <= k:
                return "YES"

        lastseen[arr[i]] = i

    return "NO"



arr=[7, 12, 5, 7, 12, 9, 12, 4]
k=2

print(repeatedlogin(arr, k))
