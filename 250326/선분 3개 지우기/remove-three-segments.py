def reset(n:int, arr: list[int]) -> None:
    for i in range(n):
        arr[i] = 0


def find_non_overlapping_lines(n:int, lines:list[tuple[int]]) -> int:
    # TC = O(N^4) = O(10^4) == 500ms
    # SC = O(M) = 100 * 4bytes == 0.4KB
    
    MAX_LENGTH = 100
    
    lines_arr = [0 for _ in range(MAX_LENGTH + 1)]
    count = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                reset(MAX_LENGTH + 1, lines_arr)

                for idx, line in enumerate(lines):
                    if idx == i or idx == j or idx == k:
                        continue

                    start, end = line
                    if lines_arr[start] or lines_arr[end]:
                        break
                    for l in range(start, end+1):
                        lines_arr[l] = 1
                else:
                    count += 1

    return count

if __name__ =="__main__":
    # For given N lines,
    # while remove 3 different lines,
    # find (n-3) lines that do not overlap each other
    # If two lines share a point, that is an overlap

    # Constratins
    # 1. 4 <= N <= 10
    # 2. 0 <= a < b <= 10^2
    # T <= 5000ms
    # S <= 288MiB

    # Approach
    # 1. Make combinations of 3 lines with nested loop O(N^3)
    # 2. for line in range(0, N)
    #       if idx_line == selected 3 lines:
    #           break
    #       else:
    #           count += 1

    n = int(input())
    lines = []
    for _ in range(n):
        start, end = map(int, input().split())
        lines.append((start, end))
    
    print(find_non_overlapping_lines(n, lines))
    