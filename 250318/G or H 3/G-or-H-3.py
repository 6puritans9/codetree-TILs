def get_max_score(n, k, peoples:list[str]) -> int:
    # This one is for utilizing sliding window
    # TC = O(NlogN) + O(2N) = O(NlogN)
    # SC = O(1)

    score = {"G":1, "H":2}

    max_score = 0
    cur_score = 0

    left = 0
    for right in range(n):
        right_pos, right_letter = peoples[right]
        cur_score += score[right_letter]

        while right_pos - peoples[left][0] > k:
            left_pos, left_letter = peoples[left]
            cur_score -= score[left_letter]
            left += 1
            
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

    n, k = map(int, input().split())
    peoples = []
    for _ in range(n):
        pos, letter = input().split()
        peoples.append((int(pos), letter))
    
    peoples.sort(key=lambda x:x[0])
    
    print(get_max_score(n, k, peoples))
