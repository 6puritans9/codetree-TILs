n, t = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))

for _ in range(t):
    temp_first = first[-1]
    temp_second = second[-1]
    temp_third = third[-1]

    for i in range(n-1, 0, -1):
        first[i] = first[i-1]
        second[i] = second[i-1]
        third[i] = third[i-1]
    
    first[0] = temp_third
    second[0] = temp_first
    third[0] = temp_second

for num in first:
    print(num, end=" ")
print()
for num in second:
    print(num, end=" ")
print()
for num in third:
    print(num, end=" ")