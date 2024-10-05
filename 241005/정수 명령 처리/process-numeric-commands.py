N = int(input())
stack = []
stack_size = 0

for _ in range(N):
    _input = input().split()

    result = None
    if len(_input) > 1:
        stack.append(int(_input[1]))
        stack_size += 1
    else:
        instruction = _input[0] 

        if instruction == "size":
            result = stack_size
        elif instruction == "pop":
            result = stack[-1]
            del stack[-1]
            stack_size -= 1
        elif instruction == "empty":
            result = 0 if stack_size else 1
        else:
            result = stack[-1]

    if result or result == 0:
        print(result)