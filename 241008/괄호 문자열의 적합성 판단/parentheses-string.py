string = [char for char in input()]
stack = []
is_correct = "Yes"

for char in string:
    if char == "(":
        stack.append(char)
    else:
        if stack[-1] == "(":
            stack.pop()
        else:
            is_correct = "No"
            break

if len(stack) > 0:
    is_correct = "No"

print(is_correct)