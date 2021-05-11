import random


class SelectionSort:

    @staticmethod
    def sort(arr):
        arr_len = len(arr)
        for i in range(arr_len):
            min_index = i
            for j in range(i, arr_len):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


arr = [random.randrange(1, 1000000, 1) for i in range(500000)]
arr = [2, 1, -1, 8, 6, 6, 99, 30, 10, 7, 44, 99, 4]
print(SelectionSort.sort(arr))
