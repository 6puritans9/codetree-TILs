def get_deci(binary, n) -> int:
    deci = 0
    for i in range(n-1, -1, -1):
        deci += binary[i] * (2 ** ((n -1) - i))
    
    return deci


def find_max(binary) -> int:
    n = len(binary)
    result = -1

    for i in range(n):
        if not binary[i]:
            binary[i] = 1
            result = max(result, get_deci(binary, n))
            binary[i] = 0
        else:
            binary[i] = 0
            result = max(result, get_deci(binary, n))
            binary[i] = 1

    return result


if __name__ == "__main__":
    binary = [int(num) for num in str(input())]

    print(find_max(binary))