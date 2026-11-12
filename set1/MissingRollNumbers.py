def misiingnumber(arr):
    n=len(arr)
    for i in range(1,n+1):
        if i not in arr:
            return i  
arr=[1,2,3,4,6]
print(misiingnumber(arr))  # Output: 5