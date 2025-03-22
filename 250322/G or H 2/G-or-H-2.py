def find_max_len(n:int, people:list[int, str]) -> int:
    global MAX_POS

    # TC = O(MAX_POS^3)
    # SC = O(MAX_POS)

    people_arr = [None for _ in range(MAX_POS + 1)]
    for pos, char in people:
        people_arr[pos] = char

    max_len = 0
    for end in range(1, MAX_POS + 1):
        for start in range(1, end):
            if not people_arr[start] or not people_arr[end]:
                continue
            count_g, count_h = 0, 0

            for k in range(start, end + 1):
                char = people_arr[k]
                if char == 'G':
                    count_g += 1
                if char == 'H':
                    count_h += 1
            
            if count_g == 0 or count_h == 0 or count_g == count_h:
                max_len = max(max_len, end-start)

    return max_len


if __name__ == "__main__":
    # N people are standing in their unique position holding 'G' or 'H'.
    # Find the length of continuous subarray,
    # which consists of either just 'G' or 'H'
    # or contains the same number of 'G' and 'H' for each.
    # If there's only one element in the subarray, the length is 0.

    # Constraints:
    # 1 <= N <= 100
    # 0 <= pos <= 100
    # For each unique pos, 'G' or 'H' do not overlap
    # length = end - start

    # Approach:
    # 1. It seems sliding window is not feasible for this problem
    # 2. A nested iteration is needed to set the start and end
    # 3. and an additional iteration is needed for iteration between (start, end + 1) O(N^3)
    # 3. Make an array of each person in people
    # 4. check the count of 'G' or 'H' whether they are same or only one of them is included
        
    MAX_POS = 100

    n = int(input())
    people = []
    for _ in range(n):
        pos, char = input().split()
        people.append((int(pos), char))
    
    print(find_max_len(n, people))