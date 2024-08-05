def recursion(n):
    if n < 1:
        return

    print(n, end=" ")
    recursion(n -1)
    print(n, end=" ")


N = int(input())
recursion(N)