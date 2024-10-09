from collections import deque


N = int(input())
q = deque()

for _ in range(N):
    _input = input().split()

    if len(_input) > 1:
        instruction, value = _input

        if instruction == "push_front":
            q.appendleft(value)
        else:
            q.append(value)
                
        continue
    
    instruction = _input[0]

    if instruction == "pop_front":
        print(q.popleft())
    elif instruction == "pop_back":
        print(q.pop())
    elif instruction == "size":
        print(len(q))        
    elif instruction == "empty":
        print(1) if not len(q) else print(0)
    elif instruction == "front":
        print(q[0])
    else:
        print(q[-1])