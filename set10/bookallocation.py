
def can_allocate(pages, m, limit):
    groups = 1
    current_pages = 0

    for p in pages:
        if current_pages + p <= limit:
            current_pages += p
        else:
            groups += 1
            current_pages = p

    return groups <= m


def book_allocation(pages, n, m):
    if m > n:
        return -1

    low = pages[0]
    high = 0

    # Find largest individual book and total pages
    for p in pages:
        if p > low:
            low = p

        high += p

    ans = high

    while low <= high:
        mid = (low + high) // 2

        if can_allocate(pages, m, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


# Main
arr=[25, 46, 28, 49, 24, 20]
group=3
print(book_allocation(arr, len(arr), 3))
