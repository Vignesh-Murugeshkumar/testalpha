def combined_attendee(A, B):
    i = j = k = 0
    result = [0] * (len(A) + len(B))
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            result[k] = A[i]
            i += 1
        elif A[i] > B[j]:
            result[k] = B[j]
            j += 1
        else:
            result[k] = A[i]
            i += 1
            j += 1
        k += 1
    while i < len(A):
        result[k] = A[i]
        i += 1
        k += 1
    while j < len(B):
        result[k] = B[j]
        j += 1
        k += 1
    return result[:k]
A = [3, 8, 12, 20, 25]
B = [5, 8, 20, 31]

print(combined_attendee(A, B))