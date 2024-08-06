def fact(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    
    return n * fact(n-1)

N = int(input())
print(fact(N))