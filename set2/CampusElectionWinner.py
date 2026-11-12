def campuselectionwinner(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
        if freq[num]>len(arr)//2:
            return num
arr = [3, 2, 3, 3, 1, 3, 2, 3, 3]

print(campuselectionwinner(arr))