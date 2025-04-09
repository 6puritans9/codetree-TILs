def find_min_dist(a, b, x, y) -> int:
    min_dist = float("inf")

    # a >> x >> y >> b
    steps1 = abs(a-x) + abs(b-y)
    min_dist = min(min_dist, steps1)
    

    # a >> y >> x >> b
    steps2 = abs(a-y) + abs(b-x)
    min_dist = min(min_dist, steps2)


    # a >> b
    min_dist = min(min_dist, abs(b-a))

    return min_dist


if __name__ == "__main__":
    a, b, x, y = map(int, input().split())
    print(find_min_dist(a,b,x,y))