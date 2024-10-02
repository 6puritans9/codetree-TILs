def heapify(arr, n, start_idx):
    # All indices
    largest = start_idx
    child_L = start_idx * 2
    child_R = (start_idx * 2) + 1

    if child_L <= n and arr[child_L] > arr[largest]:
        largest = child_L
    if child_R <= n and arr[child_R] > arr[largest]:
        largest = child_R

    if largest != start_idx:
        arr[start_idx], arr[largest] = arr[largest], arr[start_idx]
        heapify(arr, n, largest)


def heap_sort(arr, n):
    for i in range(n, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(arr, i-1, 1)


n = int(input())
inputs = list(map(int, input().split()))
numbers = [0]

for _input in inputs:
    numbers.append(_input)

# init
for i in range(n // 2, 0, -1):
    heapify(numbers, n, i)

# sort
heap_sort(numbers, n)

for number in numbers[1:]:
    print(number, end=" ")