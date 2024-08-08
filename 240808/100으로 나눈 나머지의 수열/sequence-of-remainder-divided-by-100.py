def recursion(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    
    return (recursion(n - 1) * recursion(n - 2)) % 100

n = int(input())

print(recursion(n))