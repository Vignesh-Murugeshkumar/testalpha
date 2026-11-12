"""Find the second highest sensor reading in an array of integers."""
# Input: 9
# 31 28 35 35 29 -4 35 28 30
# Sample output:
# 31    

def secondhighestreading(arr):

    

    largest = float('-inf')
    second = float('-inf')  

    for num in arr:
        if num > largest:
            second = largest
            largest = num

        elif num < largest and num > second:
            second = num

    if second == float('-inf'):
        print("None")
    else:
        print(second)
arr = [31, 28, 35, 35, 29, -4, 35, 28, 30]
print(secondhighestreading(arr))  # Output: 31