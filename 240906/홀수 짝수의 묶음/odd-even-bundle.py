N = int(input())
numbers = list(map(int, input().split()))

odds = sum(1 for num in numbers if num % 2 == 1)
evens = N - odds

if evens == 0:
    ans = odds // 2
elif odds == 0:
    ans = 1
else:
    ans = min(evens, odds) + 1
    
    if odds > evens:
        ans += (odds - evens) // 2

print(ans)