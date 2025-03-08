def print_pairs(n:int, string:list[str]) -> int:
    # Time complexity = O(n)
    # Space complexity = O(n)

    stack = []

    count = 0
    for i in range(n-1):
        if string[i] == "(" and string[i+1] == "(":
            openings = (string[i], string[i+1])
            stack.append(openings)
        
        elif string[i] == ")" and string[i+1] == ")" and len(stack):
            count += len(stack)

    return count


if __name__ == "__main__":
    # Find the pairs: '(', ')'
    # Push consecutive openings into a stack,
    # and if consecutive closings follows at some point, 
    # count += len(stack)
    
    string = [char for char in input()]
    n = len(string)

    print(print_pairs(n, string))