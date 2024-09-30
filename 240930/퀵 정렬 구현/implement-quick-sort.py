def select_pivot(low_val, mid_val, high_val):
    median = None

    if low_val > mid_val and low_val < high_val or low_val > high_val and low_val < mid_val:
        median = low_val
    elif mid_val > low_val and mid_val < high_val or mid_val > high_val and mid_val < low_val:
        median = mid_val
    else:
        median = high_val

    return median


def partition(arr, low, mid, high):
    i, j = low - 1, low
    pivot_val = select_pivot(arr[low], arr[mid], arr[high])
    pivot_idx = None
    if pivot_val == arr[low]:
        pivot_idx = low
    elif pivot_val == arr[mid]:
        pivot_idx = mid
    else:
        pivot_idx = high

    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

    while j <= high:
        if arr[j] < pivot_val:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        j += 1

    i += 1
    arr[i], arr[high] = arr[high], arr[i]

    return i


def quicksort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        pivot = partition(arr, low, mid, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)


n = int(input())
numbers = list(map(int, input().split()))

quicksort(numbers, 0, n - 1)
for number in numbers:
    print(number, end=" ")