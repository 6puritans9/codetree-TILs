def get_combinations(n, m, start, array):
    global answers

    if len(array) == m:
        number = "".join(map(str, array))
        answers.append(number)
        return

    for i in range(start, n+1):
        array.append(i)
        get_combinations(n, m, i + 1, array)
        array.pop()


if __name__ == "__main__":
    n, m = tuple(map(int, input().split()))
    answers = []
    get_combinations(n, m, 1, [])

    for elem in answers:
        print(" ".join(elem)) if int(elem) > n else print("".join(elem))
