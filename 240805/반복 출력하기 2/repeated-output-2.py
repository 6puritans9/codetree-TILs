def recursion(n):
    if n < 1:
        return

    print("HelloWorld")
    recursion(n - 1)

N = int(input())
recursion(N)