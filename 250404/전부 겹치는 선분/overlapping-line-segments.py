def are_all_lines_overlap(n:int, lines:list[int]) -> str:
    # TC = O(N*MAX_LIMIT)
    # SC = O(MAX_LIMIT)

    MAX_LIMIT = 100
    
    result = ["No", "Yes"]
    dimension = [0 for _ in range(MAX_LIMIT+1)]

    for x1, x2 in lines:
        for i in range(x1, x2+1):
            dimension[i] += 1
    
    for x in dimension:
        if x == n:
            return result[1]
    
    return result[0]


if __name__ == "__main__":
    # N lines are on 1-dimension
    # Find whether there is a point that every line overlaps or not
    # if two lines share a point on their edge, that is an overlap

    # Constraints
    # 2 <= N <= 10^2
    # 1 <= x1 <= x2 <= 10^2
    # Time 5000ms
    # Space 288MiB

    # Approach
    # 1. Assign an empty array which represents the dimension
    # 2. for each (x1, x2):
    #       for x in range(x1, x2+1):
    #           arr[x] += 1
    # 3. find if there's arr[x] == N

    n = int(input())
    lines = []
    for _ in range(n):
        x1, x2 = map(int, input().split())
        lines.append((x1, x2))

    print(are_all_lines_overlap(n, lines))
