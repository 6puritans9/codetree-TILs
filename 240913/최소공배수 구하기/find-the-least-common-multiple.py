n, m = tuple(map(int, input().split()))
max_num = max(n, m)

ans = 0
for i in range(max_num, n*m + 1):
    if not i % n and not i % m:
        ans = i
        break

print(i)