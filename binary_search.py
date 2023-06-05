from quick_sort import QuickSort

class BinarySearch:


    def __init__(self, arr: list) -> None:
        self.arr = arr
        self.__iterations = 0

    @staticmethod
    def search_element(arr, item):
        left_border = 0
        right_border = len(arr) - 1

        while left_border <= right_border:
            middle_position = int((left_border + right_border) / 2)
            middle_element = arr[middle_position]

            if item == middle_element:
                print(f"Item found at position {middle_position}")
                return middle_position
            else:
                if item < middle_element:
                    right_border = middle_position - 1
                else:
                    left_border = middle_position + 1
        return None

    def call_search(self, item):
        """Calls search method"""

        self.__iterations += 1
        return BinarySearch.search_element(self.arr, item)

if __name__ == "__main__":
    bs = BinarySearch([2, 5, 8, 3, 12, 4, 7])
    print(bs.call_search(12))

