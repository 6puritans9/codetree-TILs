def get_combinations(k, n, ans, idx):
    if idx == n:
        print(" ".join(map(str, ans)))
        return

    for i in range(1, k + 1):
        if n >= 3 and idx >= 2:
            if i == ans[idx - 1] and ans[idx - 1] == ans[idx - 2]:
                continue

        ans.append(i)
        get_combinations(k, n, ans, idx + 1)
        ans.pop()


if __name__ == "__main__":
    k, n = tuple(map(int, input().split()))
    ans = []

    get_combinations(k, n, ans, 0)