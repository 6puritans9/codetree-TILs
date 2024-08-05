def recursive_sum(n):
    if n < 1:
        return 0
    
    return n + recursive_sum(n-1)

N = int(input())
print(recursive_sum(N))