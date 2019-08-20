from common.interfaces.stack import Stack


class LinkedListStack(Stack):
    # region Node Class

    class LinkedListNode:
        def __init__(self, item):
            self.__item = item
            self.__next = None

        @property
        def item(self):
            return self.__item

        @property
        def next(self):
            return self.__next

        @next.setter
        def next(self, value):
            self.__next = value

    # endregion

    # region Init

    def __init__(self):
        self.__first = None
        self.__size = 0

    # endregion

    # region Public Methods

    def pop(self):
        if self.__first is None:
            return None
        item = self.__first.item
        self.__first = self.__first.next
        self.__size -= 1
        return item

    def push(self, item):
        old_first = self.__first
        self.__first = LinkedListStack.LinkedListNode(item)
        self.__first.next = old_first
        self.__size += 1

    def peek(self):
        if self.__first is None:
            return None
        return self.__first.item

    def clear(self):
        self.__first = None
        self.__size = 0

    def is_empty(self):
        return self.__first is None

    def get_size(self):
        return self.__size

    # endregion

    # region Iterator

    def __iter__(self):
        self.__current = LinkedListStack.LinkedListNode(None)
        self.__current.next = self.__first
        return self

    def __next__(self):
        self.__current = self.__current.next
        if self.__current is None:
            raise StopIteration
        else:
            return self.__current.item

    # endregion

    # region Str And Repr

    def __str__(self):
        output = ""
        for current in self:
            output += f"{current}\n"
        return output

    def __repr__(self):
        return self.__str__()

    # endregion


if __name__ == '__main__':
    pass
