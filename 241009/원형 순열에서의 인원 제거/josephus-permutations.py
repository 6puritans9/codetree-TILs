from collections import deque


N, K = list(map(int, input().split()))
q = deque()
for i in range(1, N + 1):
    q.append(i)

while N > 1:
    for _ in range(K - 1):
        q.append(q.popleft())
    
    print(q.popleft(), end=" ")
    N -= 1

print(q[0])