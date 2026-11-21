def exammarksrankingbycounting(n, scores):
    max_score = max(scores)
    min_score = min(scores)
    range_of_scores = max_score - min_score + 1
    count = [0] * range_of_scores
    for score in scores:
        count[score - min_score] += 1
    result = []
    for i in range(range_of_scores):
        for _ in range(count[i]):
            result.append(i + min_score)
    return result
arr = [40, 25, 60, 25, 90, 75, 60, 30, 50]
n = len(arr)
print(exammarksrankingbycounting(n, arr))