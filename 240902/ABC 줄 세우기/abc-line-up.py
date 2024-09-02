n = int(input())
peoples = list(input().split())

count = 0
for i in range(n):
    for j in range(n - 1 - i):
        if peoples[j] > peoples[j + 1]:
            peoples[j], peoples[j + 1] = peoples[j+1], peoples[j]
            count += 1

print(count)