from collections import deque


N = int(input())
numbers = deque([i for i in range(1, N+1)])

while N > 1:
    numbers.popleft()
    numbers.append(numbers.popleft())
    N -=1

print(numbers[0])