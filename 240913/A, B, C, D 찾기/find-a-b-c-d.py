numbers = list(map(int, input().split()))
numbers.sort()

a = numbers[0]
b = numbers[1]
c = numbers[2]
d = numbers[-1] - (a + b + c)

print(a, b, c, d)