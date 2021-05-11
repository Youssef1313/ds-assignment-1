import random
import time


class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        start: float = time.process_time()
        self.__sort_alg()
        end: float = time.process_time()
        print(end-start)
        return self.arr

    def __sort_alg(self):
        arr_len = len(self.arr)
        for i in range(arr_len):
            min_index = i
            for j in range(i, arr_len):
                if self.arr[min_index] > self.arr[j]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]


arr = [random.randrange(1, 1000000, 1) for i in range(500000)]
# arr = [2, 1, -1, 8, 6, 6, 99, 30, 10, 7, 44, 99, 4]
ss = SelectionSort(arr)
print(ss.sort())

