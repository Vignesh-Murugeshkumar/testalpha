def PlagiarismPatternScanner(arr1, arr2):
    s, p = arr1, arr2
    n, m = len(s), len(p)

    if m > n:
        return "None"

    bal = [0] * 26              # window count minus needed count
    for ch in p:
        bal[ord(ch) - 97] -= 1

    diff = sum(1 for v in bal if v != 0)   # letters whose counts mismatch
    res = []

    for i in range(n):
        # add the incoming character
        c = ord(s[i]) - 97
        if bal[c] == 0:
            diff += 1
        bal[c] += 1
        if bal[c] == 0:
            diff -= 1

        # remove the outgoing character
        if i >= m:
            c = ord(s[i - m]) - 97
            if bal[c] == 0:
                diff += 1
            bal[c] -= 1
            if bal[c] == 0:
                diff -= 1

        # window s[i-m+1 .. i] is complete
        if i >= m - 1 and diff == 0:
            res.append(i - m + 1)

    return " ".join(map(str, res)) if res else "None"

arr1 = "abcbac"
arr2 = "abc"
print(PlagiarismPatternScanner(arr1, arr2))
