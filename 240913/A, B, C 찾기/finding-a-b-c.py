sums = list(map(int, input().split()))
sums.sort()

a, b = sums[0], sums[1]
c = 0
for i in range(sums[2], sums[-1]):
    if b + i == sums[-2]:
        c = i

print(a, end=" ")
print(b, end=" ")
print(c, end=" ")