N = int(input())
numbers = list(map(int, input().split()))

odds = []
len_odds = 0
evens = []
len_evens = 0
for number in numbers:
    if number % 2:
        odds.append(number)
        len_odds += 1
    else:
        evens.append(number)
        len_evens += 1

ans = 0
if not len_evens:
    ans = len_odds // 2
elif len_evens < len_odds:
    if len_evens == 1:
        ans = len_odds - 1
    else:
        ans = len_odds + 1
elif len_evens > len_odds:
    ans = (len_evens // 2 + 1) + len_odds
else:
    ans = len_evens + len_odds

print(ans)