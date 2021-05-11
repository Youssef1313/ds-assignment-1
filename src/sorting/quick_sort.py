import random
import time


class QuickSortLP:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        start: float = time.process_time()
        self.__quick_sort_last_piviot(0, len(self.arr))
        end: float = time.process_time()
        print(end-start)
        return self.arr

    def __quick_sort_last_piviot(self, first, last):
        if first >= last:
            return
        p: int = self.__partition_last_piviot(first, last - 1)
        self.__quick_sort_last_piviot(first, p)
        self.__quick_sort_last_piviot(p + 1, last)

    def __partition_last_piviot(self, first, last):
        i: int = first - 1
        j: int = first
        piv: int = self.arr[last]

        while i < (last) and j < (last):
            if self.arr[j] < piv:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            j += 1
        self.arr[i + 1], self.arr[last] = self.arr[last], self.arr[i + 1]
        return i+1


class QuickSortRP:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        start: float = time.process_time()
        self.__quick_sort_random_piviot(0, len(self.arr))
        end: float = time.process_time()
        print(end-start)
        return self.arr

    def __quick_sort_random_piviot(self, first, last):
        if first >= last:
            return
        p: int = self.__partition_random_piviot(first, last - 1)
        self.__quick_sort_random_piviot(first, p)
        self.__quick_sort_random_piviot(p + 1, last)

    def __partition_random_piviot(self, first, last):
        rand: int = random.randint(first, last)
        i: int = first - 1
        j: int = first
        piv: int = self.arr[rand]

        while i < (last) and j < (last):
            if self.arr[j] < piv:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            j += 1
        self.arr[i + 1], self.arr[rand] = self.arr[rand], self.arr[i + 1]
        return i+1


arr = [random.randrange(1, 1000000, 1) for i in range(500000)]
q1 = QuickSortLP(arr)
q2 = QuickSortRP(arr)
q1.sort()
q2.sort()
# print(q1.sort())
# print(q2.sort())
