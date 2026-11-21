def squaretilefloorplanner(n):
    if n <= 0:
        return 0
    for i in range(1, n + 1):
        if i * i > n:
            return i - 1
    return n
print(squaretilefloorplanner(99))