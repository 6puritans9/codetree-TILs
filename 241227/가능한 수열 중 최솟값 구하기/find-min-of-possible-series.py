def is_duplicate(sequence):
    length = len(sequence)
    for sub_len in range(1, length // 2 + 1):
        if sequence[-sub_len:] == sequence[-2 * sub_len:-sub_len]:
            return True
    return False

def get_sequence(n):
    array = []
    for _ in range(n):
        for num in [4, 5, 6]:
            array.append(num)
            if is_duplicate(array):
                array.pop()
            else:
                break
    return array

if __name__ == "__main__":
    n = int(input())
    sequence = get_sequence(n)
    print("".join(map(str, sequence)))
