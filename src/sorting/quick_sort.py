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
        piv_ind = self._get_pivot(first, last)
        piv = piv_ind[0]
        ind = piv_ind[1]
        self.arr[ind], self.arr[last] = self.arr[last], self.arr[ind]
        while i < (last) and j < (last):
            if self.arr[j] < piv:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            j += 1
        self.arr[i + 1], self.arr[last] = self.arr[last], self.arr[i + 1]
        return i + 1

    @abstractmethod
    def _get_pivot(self, first, last):
        pass


class QuickSortLP(QuickSort):
    def __init__(self, arr):
        self.arr = arr

    def _get_pivot(self, first, last):
        return self.arr[last], last


class QuickSortRP(QuickSort):
    def __init__(self, arr):
        self.arr = arr

    def _get_pivot(self, first, last):
        rand: int = random.randint(first, last)
        return self.arr[rand], rand


# arr = [random.randrange(1, 1000000, 1) for i in range(500000)]
arr = [5, 3.1, 3, 5.5, 1, 2.1, 3.0, 1]
q1 = QuickSortLP(arr)
q2 = QuickSortRP(arr)
print(q1.sort())
print(q2.sort())
