def is_beautiful(current):
    length = len(current)
    i = 0
    while i < length:
        digit = current[i]
        count = 0
        while i + count < length and current[i + count] == digit:
            count += 1
        if count != int(digit):
            return False
        i += count
    return True

def backtrack(n, current, count):
    if len(current) == n:
        if is_beautiful(current):
            count[0] += 1
        return
    
    for digit in "1234":
        backtrack(n, current + digit, count)

def count_beautiful_numbers(n):
    count = [0]
    backtrack(n, "", count)
    return count[0]


n = int(input())
print(count_beautiful_numbers(n))
