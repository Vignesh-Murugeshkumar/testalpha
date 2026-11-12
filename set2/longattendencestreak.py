def longattendencestrak(arr,t):
    longest_streak = 0
    current_streak = 0
    for i in range(len(arr)):
        if arr[i] >= t:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 0
    return longest_streak
arr=[28,35,40,31,30,12,33,36,29,41]
t=30
print(longattendencestrak(arr,t))  # Output: 4