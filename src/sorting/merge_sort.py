def merge_sort(unsorted):
    if len(unsorted) <= 1:
        return

    unsorted_half1, unsorted_half2 = divide(unsorted)
    merge_sort(unsorted_half1)
    merge_sort(unsorted_half2)
    merge(unsorted_half1, unsorted_half2, unsorted)


def divide(unsorted):
    half_i = len(unsorted) // 2
    return unsorted[:half_i], unsorted[half_i:]


def merge(sorted_half1, sorted_half2, unsorted):
    i, j, k = 0, 0, 0
    half1_length, half2_length = len(sorted_half1), len(sorted_half2)

    while i != half1_length and j != half2_length:
        if sorted_half1[i] < sorted_half2[j]:
            unsorted[k] = sorted_half1[i]
            i += 1
        else:
            unsorted[k] = sorted_half2[j]
            j += 1
        k += 1

    unsorted[k:] = sorted_half1[i:] if i != half1_length else sorted_half2[j:]
