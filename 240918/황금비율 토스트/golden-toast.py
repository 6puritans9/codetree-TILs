from collections import deque


def move(pos, instruction):
    global letters_left
    global letters_right
    global n
    new_pos = pos

    if instruction == "L" and pos != 0:
        letters_right.appendleft(letters_left.pop())
        new_pos -= 1
    elif instruction == "R" and pos != n:
        letters_left.append(letters_right.popleft())
        new_pos += 1

    return new_pos


def delete(pos):
    global letters_right
    global n

    if pos != n:
        letters_right.popleft()
        n = n-1


def insert(pos, letter):
    global letters_left
    global n
    
    letters_left.append(letter)
    n += 1
    new_pos = pos + 1
    
    return new_pos


n, m = map(int, input().split())
letters_left = deque([char for char in input()])
letters_right = deque()
pos = n

for _ in range(m):
    _input = input().split()

    if len(_input) > 1:
        instruction, letter = _input
    else:
        instruction = _input[0]
    
    if instruction == "L" or instruction == "R":
        pos = move(pos, instruction)
    elif instruction == "D":
        delete(pos)
    else:
        pos = insert(pos, letter)

letters_left.extend(letters_right)
for letter in letters_left:
    print(letter, end="")