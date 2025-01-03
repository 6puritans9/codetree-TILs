def generate_permutations(n, permutation):
    if len(permutation) == n:
        print(" ".join(map(str, permutation)))
        return
    
    for i in range(1, n+1):
        if i not in permutation:
            permutation.append(i)
            generate_permutations(n, permutation)
            permutation.pop()

    # generate_permutations(n, idx + 1, permutation)


if __name__ == "__main__":
    n = int(input())
    generate_permutations(n, [])
    