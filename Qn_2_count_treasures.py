def count_treasures(s, queries):
    prefix_count = [0] * (len(s) + 1)
    for i in range(len(s)):
        prefix_count[i + 1] = prefix_count[i] + (1 if s[i] == 'T' else 0)

    results = []
    for start, end in queries:
        treasure_count = prefix_count[end] - prefix_count[start - 1]
        results.append(treasure_count)

    return results


s = input("Enter the path string (e.g., T..T.T): ")
n = int(input("Enter the number of queries: "))
queries = []
for _ in range(n):
    start, end = map(int, input("Enter start and end indices (e.g., 1 5): ").split())
    queries.append((start, end))


results = count_treasures(s, queries)
print("Results for each query:")
for result in results:
    print(result)
