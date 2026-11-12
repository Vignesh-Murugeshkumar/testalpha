
def DailySalesRangeReports(sales, p, q):

    n = len(sales)

    prefix = [0] * n
    prefix[0] = sales[0]

    # Build prefix sum array
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + sales[i]

    # Process queries
    for i in range(q):

        l, r = p[i]

        if l == 0:
            print(prefix[r])
        else:
            print(prefix[r] - prefix[l - 1])


sales = [5, 3, 8, 2, 7, 1, 9, 4]


p = [(0, 2), (2, 5), (1, 7)]
DailySalesRangeReports(sales, p, 3)
