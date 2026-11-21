
def moveZeroes(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1
    while pos < len(nums):
        nums[pos] = 0
        pos += 1
    return nums

arr=[0, 14, 0, 3, 7, 0, 0, 9, 5]
print(*moveZeroes(arr))


