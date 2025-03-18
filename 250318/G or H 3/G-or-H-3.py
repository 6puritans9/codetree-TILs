def get_max_score(n, k, letters:list[str]) -> int:
    # TC = O(MAX_LENGTH * K)
    # SC = O(MAX_LENGTH)
    
    global MAX_LENGTH
    
    score = {
        "G": 1,
        "H": 2
    }

    max_score = 0
    for i in range(1, MAX_LENGTH + 1 - k):
        photo_length = i + k
        cur_score = 0

        for j in range(i, photo_length + 1):
            if letters[j]:
                cur_score += score[letters[j]]
        
        max_score = max(max_score, cur_score)

    return max_score


if __name__ == "__main__":
    # A number of N people standing in a line holding 'G' or 'H'
    # If a K sized photo taken, G gets 1 and H gets 2.
    # Find the maximum point a photo can hold
    # size K = Larger x - Smaller x

    # 1 <= N <= 100
    # 1 <= array size <= 10000
    # 1 <= K <= 10000
    # No duplicate indices for each people, letter only be in either of 'G' and 'H'

    # from index i(i>0), create each k sized array, and compare one by one
    # since the length could be up to 10k, O(n^2) will make it in the due time

    MAX_LENGTH = 10000

    n, k = map(int, input().split())
    letters = [None for _ in range(MAX_LENGTH + 1)]
    for _ in range(n):
        pos, letter = input().split()
        letters[int(pos)] = letter
    
    print(get_max_score(n, k, letters))
