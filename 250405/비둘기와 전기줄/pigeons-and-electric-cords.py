def find_dove_moves(n:int, doves:list[int]) -> int:
    # TC = O(N)
    # SC = O(1)

    MAX_DOVE = 10
    
    positions = [-1 for _ in range(MAX_DOVE + 1)]
    count = 0

    for dove, pos in doves:
        if positions[dove] == -1:
            positions[dove] = pos
            continue
        else:
            if positions[dove] == pos:
                continue
            
            positions[dove] = pos
            count += 1

    return count


if __name__ == "__main__":
    # 10 doves are switching their places on 2 lines.
    # 0 for left, 1 for right.
    # For N times, the position of a certain dove is given.
    # Find out how many times doves have crossed the lines.

    # Constratins
    # 1 <= N <= 10^2
    # 1 <= dove <= 10
    # Time 5000ms
    # Space 288MiB

    # Approach
    # 1. Assingn an array size of 10 that indicates the position
    #       initialize it with -1
    # 2. If dove moved, check if -1
    #       if not, check pos == new pos
    # 3. count += 1
    # 4. return count

    n = int(input())
    doves = []
    for _ in range(n):
        dove, pos = map(int, input().split())
        doves.append((dove, pos))

    print(find_dove_moves(n, doves))