def recursion(num):
    if num == 1:
        return num
    elif num == 2:
        return num

    return recursion(num // 3) + recursion(num - 1)


n = int(input())
print(recursion(n))