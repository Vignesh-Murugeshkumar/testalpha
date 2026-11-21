
def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        # Skip non-alphanumeric characters from left
        if not s[left].isalnum():
            left += 1
            continue

        # Skip non-alphanumeric characters from right
        if not s[right].isalnum():
            right -= 1
            continue

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return "YES"



s="was it a car or a cat I saw"
print(isPalindrome(s))  # Output: True