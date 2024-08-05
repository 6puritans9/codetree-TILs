def recursive_star(n):
    if n < 1:
        return
    
    recursive_star(n-1)
    print("*" * n)

N = int(input())
recursive_star(N)