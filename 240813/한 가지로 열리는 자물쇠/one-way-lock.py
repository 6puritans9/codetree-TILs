def find_combinations(n, a, b, c):
    variants = 0

    for i in range (1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if a - 2 <= i <= a + 2:
                    variants += 1

                elif b - 2 <= j <= b + 2:
                    variants += 1
                
                elif c - 2 <= k <= c + 2:
                    variants += 1

    return variants


N = int(input())
a, b, c = tuple(map(int, input().split()))

print(find_combinations(N, a, b, c))