def get_fibo_recur(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    return get_fibo_recur(n-2) + get_fibo_recur(n-1)


N = int(input())
print(get_fibo_recur(N))