def blast(bombs, i, j):
    for idx in range(i, j):
        bombs[idx] = 0

    return True


if __name__ == "__main__":
    n, m = tuple(map(int, input().split()))
    bombs = [int(input()) for _ in range(n)]

    while True:
        bombs_count = len(bombs)
        exploded = False

        for i in range(bombs_count):
            if not bombs[i]:
                continue
            target_bomb = bombs[i]
            count = 1

            for j in range(i + 1, bombs_count):
                if bombs[j]:
                    if bombs[j] == target_bomb:
                        count += 1
                    if j == bombs_count - 1 and count >= m:
                        # print(i, j)
                        exploded = blast(bombs, i, j + 1)
                        # print(bombs)

                    elif bombs[j] != target_bomb and count >= m:
                        exploded = blast(bombs, i, j)
                        count = 1
                    else:
                        count = 1
            
            # print(i)
        
        if not exploded:
            break
        
        
        
    # result        
    remains = 0
    for bomb in bombs:
        if bomb:
            remains += 1
    print(remains)

    # print("remaining bombs")
    if remains:
        for i in range(len(bombs) - 1, -1, -1):
            if bombs[i]:
                print(bombs[i])
            # print(bombs[i])
