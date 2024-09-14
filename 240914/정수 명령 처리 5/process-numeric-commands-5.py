N = int(input())
arr = []

for _ in range(N):
    _input = input().split()
    if len(_input) > 1:
        instruction, num = _input
        num = int(num)
    else:
        instruction = _input

    if instruction == "push_back":
        arr.append(num)
    elif instruction[0] == "pop_back":
        arr.pop()
    elif instruction[0] == "size":
        print(len(arr))
    else:
        print(arr[num - 1])