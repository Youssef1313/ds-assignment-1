def heap_sort(unsorted):
    length = len(unsorted)
    # Build a max heap
    for i in range(length // 2, -1, -1):
        heapify(unsorted, length, i)

    for i in range(length - 1, -1, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, i, 0)


def heapify(arr, length, i):
    maximum_index = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2
    if left_index < length and arr[left_index] > arr[maximum_index]:
        maximum_index = left_index

    if right_index < length and arr[right_index] > arr[maximum_index]:
        maximum_index = right_index

    if i != maximum_index:
        arr[i], arr[maximum_index] = arr[maximum_index], arr[i]
        heapify(arr, length, maximum_index)
