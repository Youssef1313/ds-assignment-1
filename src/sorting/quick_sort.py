import random
from abc import abstractmethod


class QuickSort():

    def sort(self):
        self.__quick_sort(0, len(self.arr))
        return self.arr

    def __quick_sort(self, first, last):
        if first >= last:
            return
        p: int = self.__partition(first, last - 1)
        self.__quick_sort(first, p)
        self.__quick_sort(p + 1, last)

    def __partition(self, first, last):
        i: int = first - 1
        j: int = first
        piv: int = self._get_piviot(first, last)
        while i < (last) and j < (last):
            if self.arr[j] < piv:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            j += 1
        self.arr[i + 1], self.arr[last] = self.arr[last], self.arr[i + 1]
        return i+1

    @abstractmethod
    def _get_piviot(self, first, last):
        pass


class QuickSortLP(QuickSort):
    def __init__(self, arr):
        self.arr = arr

    def _get_piviot(self, first, last):
        return self.arr[last]


class QuickSortRP(QuickSort):
    def __init__(self, arr):
        self.arr = arr

    def _get_piviot(self, first, last):
        rand: int = random.randint(first, last)
        return self.arr[rand]


# arr = [random.randrange(1, 1000000, 1) for i in range(500000)]
arr = [2, 1, -1, 8, 6, 6, 99, 30, 10, 7, 44, 99, 4]
q1 = QuickSortLP(arr)
q2 = QuickSortRP(arr)
print(q1.sort())
print(q2.sort())














