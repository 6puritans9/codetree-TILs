def find_min_dist(n:int, peoples:list[int]) -> int:
    min_dist = float("inf")

    for start in range(n):
        total_dist = 0
        for j, people in enumerate(peoples):
            dist = (j + n - start) % n
            total_dist += (dist * people)

        min_dist = min(min_dist, total_dist)

    return min_dist


if __name__ == "__main__":
    n = int(input())
    peoples = [int(input()) for _ in range(n)]

    print(find_min_dist(n, peoples))