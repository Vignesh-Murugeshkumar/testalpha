def kthighestsalary(salaries,k):
    n=len(salaries)
    if k>n :
        return -1
    def partition(arr, low, high):
        pivot=arr[high]
        i=low-1
        for j in range(low, high):
            if arr[j]>=pivot:
                i+=1
                arr[i], arr[j]=arr[j], arr[i]
        arr[i+1], arr[high]=arr[high], arr[i+1]
        return i+1
    def quickselect(arr, low, high, k):
        if low==high:
            return arr[low]
        pivot_index=partition(arr, low, high)
        if k==pivot_index:
            return arr[k]
        elif k<pivot_index:
            return quickselect(arr, low, pivot_index-1, k)
        else:
            return quickselect(arr, pivot_index+1, high, k)
    return quickselect(salaries, 0, n-1, k-1)
arr=[40, 25, 60, 25, 90, 75, 60, 30, 50]
k=3
print(kthighestsalary(arr,k))