def get_counts(string) -> int:
    n = len(string)
    count = 0
    
    for i in range(n):
        for j in range(i, n):
            char = string[i]

            if char == "(" and string[j] == ")":
                count += 1

    return count


if __name__ == "__main__":
    string = input()

    print(get_counts(string))