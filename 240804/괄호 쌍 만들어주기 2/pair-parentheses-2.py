_input = input()
length = len(_input)

count = 0
for i in range(length - 1):
    start_char = _input[i]
    next_start_char = _input[i+1]
    
    if start_char == "(" and next_start_char == "(":
        for j in range(i+2, length-1):
            prev_end_char = _input[j]
            end_char = _input[j+1]
            
            if end_char == ")" and prev_end_char == ")":
                count += 1

print(count)