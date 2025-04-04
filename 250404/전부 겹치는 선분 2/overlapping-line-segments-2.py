def are_they_overlap(n:int, lines:list[int]) -> str:
    # TC = O(N^2)
    # SC = O(1)
    
    result = ["No", "Yes"]

    for i in range(n):
        max_start = 0
        min_end = float("inf")

        for j in range(n):
            if i ==j:
                continue
            
            x, y = lines[j]
            max_start = max(max_start, x)
            min_end = min(min_end, y)
        
        if max_start <= min_end:
            return result[1]
        
    return result[0]


if __name__ == "__main__":
    # N lines are on 1-dimension
    # find if there's a point on which (N-1) lines overlap
    # if a line were removed

    # Constraints
    # 3 <= N <= 10^2
    # 1 <= x1 <= x2 <= 10^2
    # Time 5000ms
    # Space 288MiB

    # Approach
    # 1. Make combinations nCn-1
    # 2. By using max_start, min_end, find if there's an overlapping point

    n = int(input())
    lines = []
    for _ in range(n):
        x1, x2 = map(int, input().split())
        lines.append((x1, x2))

    print(are_they_overlap(n, lines))

