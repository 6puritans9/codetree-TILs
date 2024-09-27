def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    merged_list = []
    
    i = low
    j = mid + 1

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            merged_list.append(arr[i])
            i += 1
        else:
            merged_list.append(arr[j])
            j += 1


    while i <= mid:
        merged_list.append(arr[i])
        i += 1
    
    while j <= high:
        merged_list.append(arr[j])
        j += 1

    for k in range(len(merged_list)):
        arr[low + k] = merged_list[k]


n = int(input())
numbers = list(map(int, input().split()))
merge_sort(numbers, 0, n - 1)

for number in numbers:
    print(number, end=" ")