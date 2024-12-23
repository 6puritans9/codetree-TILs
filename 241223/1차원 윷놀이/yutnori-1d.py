def backtrack(moves, positions, turn, score):
    global max_score, n, m, k
    
    if turn == n:
        max_score = max(max_score, score)
        return
    
    for i in range(k):
        original_position = positions[i]
        
        if positions[i] < m:
            positions[i] += moves[turn]
            
            if positions[i] >= m and original_position < m:
                backtrack(moves, positions, turn + 1, score + 1)
            else:
                backtrack(moves, positions, turn + 1, score)
            
            positions[i] = original_position
        else:
            backtrack(moves, positions, turn + 1, score)


if __name__ == "__main__":
    n, m, k = tuple(map(int, input().split()))
    moves = tuple(map(int, input().split()))
    positions = [1] * k
    max_score = 0

    backtrack(moves, positions, 0, 0)
    print(max_score)
