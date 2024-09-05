n = int(input())
integers = list(map(int, input().split()))
integers.sort()

ans = -float("inf")
zero_idx = None
positive_idx = None
for i in range(n):
    if integers[i] == 0:
        zero_idx = i

    elif integers[i] > 0:
        positive_idx = i
        break

if not positive_idx and not zero_idx:
    ans = intgers[-1] * integers[-2] * integers[-3]
elif not positive_idx and zero_idx:
    ans = 0
elif positive_idx > 1:
    ans = max(integers[0] * integers[1] * integers[-1], integers[-1] * integers[-2] * integers[-3])
elif positive_idx >= 0:
    ans = integers[-1] * integers[-2] * integers[-3]


print(ans)