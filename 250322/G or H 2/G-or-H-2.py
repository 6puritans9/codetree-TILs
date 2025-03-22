def find_max_len(n:int, people:list[int, str]) -> int:
    # O(N^2) optimization
    
    # TC = O(NlogN) + O(N^2) = O(N^2)
    # SC = O(1)

    max_len = 0
    for i in range(n):
        count_g, count_h = 0, 0
        end, _ = people[i]

        for j in range(i, -1, -1):
            start, char = people[j]
            
            if char == 'G':
                count_g += 1
            else:
                count_h += 1
            
            if not count_g or not count_h or count_g == count_h:
                max_len = max(max_len, end - start)

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
        
    n = int(input())
    people = []
    for _ in range(n):
        pos, char = input().split()
        people.append((int(pos), char))
    people.sort()
    
    print(find_max_len(n, people))