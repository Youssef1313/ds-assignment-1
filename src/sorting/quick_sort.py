import random
import sys


def quick_sort_last_pivot(arr):
    sys.setrecursionlimit(1000000)
    __quick_sort(arr, 0, len(arr), __get_pivot_last)


def quick_sort_random_pivot(arr):
    sys.setrecursionlimit(1000000)
    __quick_sort(arr, 0, len(arr), __get_pivot_random)


def __quick_sort(arr, first, last, get_pivot):
    if first >= last:
        return
    partitioning_index: int = __partition(arr, first, last - 1, get_pivot)
    __quick_sort(arr, first, partitioning_index, get_pivot)
    __quick_sort(arr, partitioning_index + 1, last, get_pivot)


def __partition(arr, first, last, get_pivot):
    i: int = first - 1
    j: int = first
    piv_ind = get_pivot(arr, first, last)
    piv = piv_ind[0]
    ind = piv_ind[1]
    arr[ind], arr[last] = arr[last], arr[ind]
    while i < (last) and j < (last):
        if arr[j] < piv:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[last] = arr[last], arr[i + 1]
    return i + 1


def __get_pivot_last(arr, first, last):
    # Suppresses the unused parameter warning. The signature of
    # this should be kept the same as __get_pivot_random.
    _ = first
    return arr[last], last


def __get_pivot_random(arr, first, last):
    rand: int = random.randint(first, last)
    return arr[rand], rand
