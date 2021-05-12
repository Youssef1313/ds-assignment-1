def selection_sort(unsorted):
    arr_len = len(unsorted)
    for i in range(arr_len):
        min_index = i
        for j in range(i, arr_len):
            if unsorted[min_index] > unsorted[j]:
                min_index = j
        unsorted[i], unsorted[min_index] = unsorted[min_index], unsorted[i]


arr = [2, 1, -1, 8, 6, 6, 99, 30, 10, 7, 44, 99, 4]
selection_sort(arr)
print(arr)
