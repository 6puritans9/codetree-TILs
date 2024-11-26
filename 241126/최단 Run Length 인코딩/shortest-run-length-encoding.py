from collections import deque

def encode(string, length):
    result = ""
    count = 1
    
    for i in range(length):
        cur_char = string[i]

        if i == length - 1:
            result += f"{cur_char}{count}"
        elif cur_char == string[i+1]:
            count += 1
        else:
            result += f"{cur_char}{count}"
            count = 1

    return result


string = deque([char for char in input()])
length = len(string)

min_length = len(encode(string, length))
for i in range(length):
    string.rotate(1)
    encoded = encode(string, length)
    min_length = min(min_length, len(encoded))

print(min_length)