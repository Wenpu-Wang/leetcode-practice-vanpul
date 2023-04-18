import random


def partition(arr, left, right):
    # Classic Version
    # pivot = arr[right]

    # Random Version
    rand_idx = random.randint(left, right)
    pivot = arr[rand_idx]
    arr[right], arr[rand_idx] = arr[rand_idx], arr[right]

    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quicksort(arr, left, right):
    if left < right:
        idx = partition(arr, left, right)
        quicksort(arr, left, idx - 1)
        quicksort(arr, idx + 1, right)


# test quicksort
# li = [2, 3, 5, 9, 8, 6]
li = [10, 7, 8, 9, 1, 5]
# li = [3, 2]
li = [n for n in range(20, 0, -1)]
print(li)
quicksort(li, 0, len(li) - 1)
print(f"sorted={li}")
