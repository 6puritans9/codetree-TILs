def recursion(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return 1+recursion(n//2)
    else:
        return 1+recursion(n//3)


N = int(input())
print(recursion(N))