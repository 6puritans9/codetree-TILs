N = int(input())
numbers = list(map(int, input().split()))

ans = N - 1
for i in range(N - 1, -1, -1):
    if numbers[i - 1] > numbers[i]:
        break
    
    ans -= 1

print(ans)