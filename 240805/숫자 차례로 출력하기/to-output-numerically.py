def ascend(n):
    if n < 1:
        return
    
    ascend(n-1)
    print(n, end=" ")


def descend(n):
    if n < 1:
        return
    
    print(n, end=" ")
    descend(n-1)


N = int(input())
ascend(N)
print()
descend(N)