def in_range(n:int, idx:int) -> bool:
    return 0 <= idx < n


def find_min_max_gap(n:int, seats:list[int]) -> int:
    # TC = O(N^2) = O(10^6) < 1000ms
    # SC = O(1)
    
    min_max = 0

    for i in range(n):
        if seats[i]:
            continue
        # set
        seats[i] = 1

        cur_dist = float("inf")
        l = 0
        while l < n:
            if seats[l]:
                r = l + 1
                while r < n and not seats[r]:
                    r += 1
                if r < n:
                    cur_dist = min(cur_dist, r - l)
                l = r
            else:
                l += 1

        min_max = max(min_max, cur_dist)

        # reset
        seats[i] = 0

    return min_max


if __name__ == "__main__":
    # For given N seats,
    # 0 stands for empty seat, 1 for occupied.
    # By putting a new person on an empty seat,
    # maximize the distance between him and the next person.

    # Constraints
    # TIME 1000ms
    # SPACE 80MiB
    # 2 <= N <= 10^3
    # At least one seated person is guaranteed

    # Approach
    # 1. swap 0 to 1 one by one
    # 2. find min_max by iterating O(N^2)
    # 3. This is the only solution using brute force to find min_max
    

    # not valid:
    # 1. for every seat in seats
    # 2. if seats[i] == 0,
    # 3. create a pair of two pointers proceeding left and right.
    # 4. If seats[j]:
    #       max_dist = max(max_dist, abs(i - j))
    # 5. repeat while linear searching

    n = int(input())
    seats = [int(num) for num in input()]
    print(find_min_max_gap(n, seats))
