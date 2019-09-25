from common.interfaces.queue import QueueBase


class LinkedListQueue(QueueBase):
    # region Node Class

    class LinkedListQueueNode:
        def __init__(self, item):
            self.__item = item
            self.__next_node = None

        @property
        def item(self):
            return self.__item

        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            self.__next_node = value

    # endregion

    # region Init

    def __init__(self):
        self.__first = None
        self.__size = 0

    # endregion

    # region Public Methods
    def enqueue(self, item):
        old_first = self.__first
        self.__first = LinkedListQueue.LinkedListQueueNode(item)
        self.__first.next_node = old_first
        self.__size += 1

    def dequeue(self):
        result = None
        if self.__first is None:
            return None
        if self.__first.next_node is None:
            result = self.__first.item
            self.__first = None
            self.__size -= 1
            return result
        previous = self.__first
        current = self.__first.next_node
        while current.next_node is not None:
            previous = current
            current = current.next_node
        result = current.item
        previous.next_node = None
        self.__size -= 1
        return result

    def peek(self):
        if self.__first is None:
            return None
        if self.__first.next_node is None:
            return self.__first.item
        current = self.__first
        while current.next_node is not None:
            current = current.next_node
        return current.item

    def clear(self):
        self.__size = 0
        self.__first = None

    def is_empty(self):
        return self.__first is None

    def get_size(self):
        return self.__size

    # endregion

    # region Private Methods

    # endregion


if __name__ == '__main__':
    pass
