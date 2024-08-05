def recursion(n):
    if n < 1:
        return

    print("* " * n)
    recursion(n -1)
    print("* " * n)


N = int(input())
recursion(N)