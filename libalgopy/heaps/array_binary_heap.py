from common.enums.binary_heap_type import BinaryHeapType
from common.interfaces.priority_queue import PriorityQueueBase


class ArrayBinaryHeap(PriorityQueueBase):
    ROOT_INDEX = 1

    # region Init

    def __init__(self, binary_heap_type=BinaryHeapType.MAX):
        self.__array = []
        self.__array.append(None)  # shift first position to index equals 1
        self.__size = 0
        if binary_heap_type == BinaryHeapType.MAX:
            self.__compare = lambda left, right: self.__array[left] < self.__array[right]
        else:
            self.__compare = lambda left, right: self.__array[left] > self.__array[right]

    # endregion

    # region Public Methods

    def insert(self, item):
        self.__size += 1
        self.__array.append(item)
        self.__swim(self.__size)

    def delete(self):
        if self.is_empty():
            return None
        current_max = self.__array[ArrayBinaryHeap.ROOT_INDEX]
        self.__exchange(1, self.__size)
        self.__size -= 1
        self.__sink(1)
        self.__array.pop(self.__size + 1)
        return current_max

    def peek(self):
        if self.__size < 1:
            return None
        return self.__array[ArrayBinaryHeap.ROOT_INDEX]

    def is_empty(self):
        return self.__size == 0

    def get_size(self):
        return self.__size

    def clear(self):
        self.__array = []
        self.__array.append(None)  # shift first position to index equals 1
        self.__size = 0

    # endregion

    # region Private Methods

    def __swim(self, k):
        while k > 1 and self.__compare(k // 2, k):
            self.__exchange(k, k // 2)
            k = k // 2

    def __sink(self, k):
        while 2 * k <= self.__size:
            j = 2 * k
            if j < self.__size and self.__compare(j, j + 1):
                j += 1
            if not self.__compare(k, j):
                break
            self.__exchange(k, j)
            k = j

    def __exchange(self, left, right):
        temp = self.__array[left]
        self.__array[left] = self.__array[right]
        self.__array[right] = temp

    # endregion


if __name__ == '__main__':
    pass
