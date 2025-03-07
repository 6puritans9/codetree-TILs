def move(n, prv_state:list[int]) -> list[int]:
    last_people = prv_state[-1]
    new_state = [0] * n

    for i in range(1, n):
        new_state[i] = prv_state[i-1]
    new_state[0] = last_people

    return new_state


def find_min_dist(n:int, peoples:list[int]) -> int:
    min_dist = float("inf")
    state = peoples

    for i in range(n):
        cur_dist = 0
        for j, people in enumerate(state):
            cur_dist += (j*people)
        min_dist = min(min_dist, cur_dist)
        state = move(n, state)

    return min_dist


if __name__ == "__main__":
    n = int(input())
    peoples = [int(input()) for _ in range(n)]

    print(find_min_dist(n, peoples))