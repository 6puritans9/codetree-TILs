# def calculate(a, b, operator):
#     if operator == "+":
#         return a + b
#     elif operator == "-":
#         return a - b
#     else:
#         return a * b


# def translate(letters, idx, numbers, n):
#     if idx == len(letters) or n > 4:
#         return
    
#     for i in range(len(letters)):
#         if letters[idx] == char:
#             numbers[idx] = n



# def compute(letters, operators):
#     numbers = [0 for _ in range(len(letters))]

#     for i in range(len(letters)):
#         translate(letters, i, numbers, 1)
#     calculate()
#     translate(letters, idx, numbers, n)
   
    


# if __name__ == "__main__":
#     string = [char for char in input()]
#     letters = []
#     operators = []
    
#     for char in string:
#         if char in "+-*":
#             operators.append(char)
#         else:
#             letters.append(char)

#     max_value = 0
#     max_value = max(max_value, compute(letters, operators))

#     print(max_value)
    
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b

def evaluate_expression(values, letters, operators):
    # Replace letters with their assigned values
    stack = [values[0]]  # Start with the first value

    for i in range(len(operators)):
        operator = operators[i]
        value = values[i + 1]
        result = calculate(stack.pop(), value, operator)
        stack.append(result)
    
    return stack[0]

def generate_combinations(idx, current_values, unique_letters, max_result, letters, operators):
    if idx == len(unique_letters):
        # Evaluate the expression with the current value combination
        letter_value_map = {unique_letters[i]: current_values[i] for i in range(len(unique_letters))}
        values = [letter_value_map[char] for char in letters]
        result = evaluate_expression(values, letters, operators)
        return max(max_result, result)
    
    for value in range(1, 5):  # Assign values 1 to 4
        current_values[idx] = value
        max_result = generate_combinations(idx + 1, current_values, unique_letters, max_result, letters, operators)
    
    return max_result

def find_maximum_result(expression):
    # Parse the expression
    letters = []
    operators = []
    for char in expression:
        if char in "+-*":
            operators.append(char)
        else:
            letters.append(char)

    # Get unique letters
    unique_letters = list(set(letters))
    max_result = float('-inf')

    # Use recursive generation of combinations
    max_result = generate_combinations(0, [0] * len(unique_letters), unique_letters, max_result, letters, operators)

    return max_result

if __name__ == "__main__":
    expression = input().strip()
    print(find_maximum_result(expression))
