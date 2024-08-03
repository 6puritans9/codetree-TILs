n = int(input())
peoples = [int(num) for num in input().split()]

min = float("inf")
for i in range(len(peoples)):
    sum = 0

    for j in range(len(peoples)):
        dist = abs(j - i)
        people = peoples[j]

        sum += people * dist
    min = sum if min > sum else min
    
print(int(min))