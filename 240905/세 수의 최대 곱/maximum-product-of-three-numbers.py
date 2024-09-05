n = int(input())
integers = list(map(int, input().split()))

ans = -float("inf")
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            computation = integers[i] * integers[j] * integers[k]            
            if computation < 0:
                continue
            
            ans = max(ans, computation)

print(ans)