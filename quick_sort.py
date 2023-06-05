import timeit
import numpy as np


class QuickSort:

    def __init__(self, arr) -> None:
        self.arr = arr
        self.iterations = 0

    @property
    def iterations(self):
        return self.__iterations
    
    @iterations.setter
    def iterations(self, item):
        self.__iterations = item

    @staticmethod
    def sort_elements(arr: list) -> list:
        """Performs sorting based on quicksort algorithm"""

        if len(arr) < 2:
            return arr

        else:
            base_element = arr[0]
            less_elements = [i for i in arr[1:] if i <= base_element]
            greater_elements = [i for i in arr[1:] if i > base_element]

            return QuickSort.sort_elements(less_elements) + [base_element] + QuickSort.sort_elements(greater_elements)

    def call_sort(self) -> list:
        """Calls sorting method"""

        self.arr = QuickSort.sort_elements(self.arr)
        self.__iterations += 1
        return self.arr


if __name__ == "__main__":
    s = QuickSort(np.random.rand(100))
    print(timeit.timeit("s.call_sort()", setup="from __main__ import s", number=100))
